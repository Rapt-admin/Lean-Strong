from random import SystemRandom
from urllib.parse import urlencode
from django.conf import settings
from oauthlib.common import UNICODE_ASCII_CHARACTER_SET
import requests
from attrs import define
import jwt
from typing import Any, Dict
import requests
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy

from rest_framework import serializers, status
from rest_framework.response import Response

from rest_framework.views import APIView
from django.shortcuts import redirect
from Lean_and_Strong.settings import env


# google_log.py


class ApplicationError(Exception):
    def __init__(self, message, extra=None):
        super().__init__(message)

        self.message = message
        self.extra = extra or {}

class PublicApi(APIView):
    authentication_classes = ()
    permission_classes = ()


class GoogleLoginRedirectApi(PublicApi):
    def get(self, request, *args, **kwargs):
        google_login_flow = GoogleRawLoginFlowService()

        authorization_url, state = google_login_flow.get_authorization_url()

        request.session["google_oauth2_state"] = state

        return redirect(authorization_url)


class GoogleLoginApi(PublicApi):
    class InputSerializer(serializers.Serializer):
        code = serializers.CharField(required=False)
        error = serializers.CharField(required=False)
        state = serializers.CharField(required=False)

    def get(self, request, *args, **kwargs):
        print("Entered GoogleLoginApi get method")

        input_serializer = self.InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data

        code = validated_data.get("code")
        error = validated_data.get("error")
        state = validated_data.get("state")

        if error is not None:
            print(f"Error received: {error}")
            return Response(
                {"error": error},
                status=status.HTTP_400_BAD_REQUEST
            )

        if code is None or state is None:
            print("Code or state is missing")
            return Response(
                {"error": "Code and state are required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        session_state = request.session.get("google_oauth2_state")

        if session_state is None:
            print("Session state is missing")
            return Response(
                {"error": "CSRF check failed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        del request.session["google_oauth2_state"]

        if state != session_state:
            print("CSRF check failed")
            return Response(
                {"error": "CSRF check failed."},
                status=status.HTTP_400_BAD_REQUEST
            )

            google_login_flow = GoogleRawLoginFlowService()

            google_tokens = google_login_flow.get_tokens(code=code)
            print(f"Google tokens received: {google_tokens}")

            id_token_decoded = google_tokens.decode_id_token()
            user_info = google_login_flow.get_user_info(google_tokens=google_tokens)

            user_email = id_token_decoded["email"]
            user = user_get(email=user_email)

            if user is None:
                return Response(
                    {"error": f"User with email {user_email} is not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

            login(request, user)

            result = {
                "id_token_decoded": id_token_decoded,
                "user_info": user_info,
            }
            
            print("User Information:")
            print(f"Name: {user_info.get('name')}")
            print(f"Email: {user_info.get('email')}")
            

            return Response(result)

##################

@define
class GoogleAccessTokens:
    id_token: str
    access_token: str

    def decode_id_token(self) -> Dict[str, str]:
        id_token = self.id_token
        decoded_token = jwt.decode(jwt=id_token, options={"verify_signature": False})
        return decoded_token


#################

class GoogleRawLoginFlowService:
    API_URI = reverse_lazy("api:google-oauth2:login-raw:callback-raw")
    print("******API_URI set")

    GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_ACCESS_TOKEN_OBTAIN_URL = "https://oauth2.googleapis.com/token"
    GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

    SCOPES = [
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid",
        
    ]

    def __init__(self):
        from .views import google_raw_login_get_credentials
        self._credentials = google_raw_login_get_credentials()
    
    def get_tokens(self, *, code: str) -> GoogleAccessTokens:
        redirect_uri = self._get_redirect_uri()

        data = {
            "code": code,
            "client_id": self._credentials.client_id,
            "client_secret": self._credentials.client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        }

        response = requests.post(self.GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)
        print("data::::::::::::::",data)

        if not response.ok:
            raise ApplicationError("Failed to obtain access token from Google.")

        tokens = response.json()
        google_tokens = GoogleAccessTokens(
            id_token=tokens["id_token"],
            access_token=tokens["access_token"]
        )

        return google_tokens

    @staticmethod
    def _generate_state_session_token(length=30, chars=UNICODE_ASCII_CHARACTER_SET):
        # This is how it's implemented in the official SDK
        rand = SystemRandom()
        state = "".join(rand.choice(chars) for _ in range(length))
        return state

    def _get_redirect_uri(self):
        # API_URI = reverse_lazy("api:google-oauth2:login-raw:callback-raw")
        # print(API_URI,"...........................................###############")

        print("_get_redirect_uri 111")
        
        domain = env('BASE_BACKEND_URL')
        print("_get_redirect_uri 222")
         # api_uri = self.API_URI
        print("_get_redirect_uri 333")
       # redirect_uri = f"{domain}{api_uri}"
        redirect_uri = "http://localhost:8000/google-callback/"
        print("_get_redirect_uri 4444")
        return redirect_uri

    def get_authorization_url(self):
        print("get_authorization_url 1111")
        redirect_uri = self._get_redirect_uri()
        print(f"Redirect URI: {redirect_uri}")

        state = self._generate_state_session_token()
        print(f"Generated state token: {state}")

        params = {
            "response_type": "code",
            "client_id": self._credentials.client_id,
            "redirect_uri": redirect_uri,
            "scope": " ".join(self.SCOPES),
            "state": state,
            "access_type": "offline",
            "include_granted_scopes": "true",
            
            "prompt": "select_account",
        }

        query_params = urlencode(params)
        authorization_url = f"{self.GOOGLE_AUTH_URL}?{query_params}"
        
        print(f"Authorization URL generated: {authorization_url}")

        return authorization_url, state

    def get_user_info(self, *, google_tokens: GoogleAccessTokens):
        access_token = google_tokens.access_token

        response = requests.get(
            self.GOOGLE_USER_INFO_URL,
            params={"access_token": access_token}
        )
        
        print("get_user_info::::::",response)

        if not response.ok:
            raise ApplicationError("Failed to obtain user info from Google.")
        user_info = response.json()
        print(f"Fetched user info: {user_info}")
        return user_info
        # return response.json()


