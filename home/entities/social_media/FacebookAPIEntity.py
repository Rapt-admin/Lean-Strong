import requests
from urllib.parse import urlencode
from django.conf import settings
import jwt
import logging
import urllib.parse
from home.models import *
from rest_framework.views import APIView
from django.urls import reverse
from Lean_and_Strong.settings import env
from django.shortcuts import redirect, render
from rest_framework import status



logger = logging.getLogger(__name__)

class FacebookAccessTokens:
    def __init__(self, access_token, id_token):
        self._access_token = access_token
        self._id_token = id_token

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    @property
    def id_token(self):
        return self._id_token

    @id_token.setter
    def id_token(self, value):
        self._id_token = value

    def decode_id_token(self):
        decoded_token = jwt.decode(self.id_token, options={"verify_signature": False})
        return decoded_token

class FacebookLoginFlowService:
    def __init__(self):
        self.client_id = settings.FACEBOOK_OAUTH2['CLIENT_ID']
        self.client_secret = settings.FACEBOOK_OAUTH2['CLIENT_SECRET']
        self.redirect_uri = settings.FACEBOOK_OAUTH2['REDIRECT_URI']
        self.authorization_url = settings.FACEBOOK_OAUTH2['AUTHORIZATION_URL']
        self.token_url = settings.FACEBOOK_OAUTH2['TOKEN_URL']
        self.user_info_url = settings.FACEBOOK_OAUTH2['USER_INFO_URL']

    def get_authorization_url(self):
        state = self._generate_state_token()
        authorization_url = (
            f"{self.authorization_url}?"
            f"client_id={self.client_id}&redirect_uri={urllib.parse.quote(self.redirect_uri, safe='')}&state={state}"
        )
        return authorization_url, state
      

    def get_tokens(self, code):
        token_url = (
            f"{self.token_url}?"
            f"client_id={self.client_id}&redirect_uri={urllib.parse.quote(self.redirect_uri, safe='')}&client_secret={self.client_secret}&code={code}"
        )
        response = requests.get(token_url)
        token_data = response.json()

        if 'error' in token_data:
            raise Exception(token_data['error']['message'])

        return token_data
    
    
    def get_user_info(self, access_token):
        user_info_url = "https://graph.facebook.com/me?fields=id,name,email&access_token=" + access_token
        response = requests.get(user_info_url)
        return response.json()

    @staticmethod
    def _generate_state_token(length=30):
        from random import SystemRandom
        import string
        return ''.join(SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))

class FacebookLoginRedirectApi(APIView):
    def get(self, request, *args, **kwargs):
        facebook_login_flow = FacebookLoginFlowService()
        authorization_url, state = facebook_login_flow.get_authorization_url()
        request.session['facebook_oauth2_state'] = state
        return redirect(authorization_url)

class FacebookLoginApi(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        state = request.GET.get('state')
        error = request.GET.get('error')
        # logger.debug(f"Code received: {code}")
        # logger.debug(f"State received: {state}")

        if error:
            logger.error("Error received from Facebook: %s", error)
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        session_state = request.session.get('facebook_oauth2_state')
        if state != session_state:
            logger.error("CSRF check failed. State mismatch: session %s, received %s", session_state, state)
            return Response({"error": "CSRF check failed."}, status=status.HTTP_400_BAD_REQUEST)
        if not code:
            logger.error("No code provided by Facebook.")
            return Response({"error": "No code provided by Facebook."}, status=status.HTTP_400_BAD_REQUEST)
           
        facebook_login_flow = FacebookLoginFlowService()
        try:
            tokens = facebook_login_flow.get_tokens(code)
        except Exception as e:
            if "This authorization code has been used" in str(e):
                logger.error("Authorization code has been used. Redirecting to re-initiate the flow.")
                return redirect(reverse('facebook-login'))
            
        # logger.debug("Access token received: %s", tokens['access_token'])
        user_info = facebook_login_flow.get_user_info(tokens['access_token'])

        user_data = urlencode({
            'name': user_info.get('name'),
            'email': user_info.get('email'),
            'loginVia':"facebook",
        })

        return redirect(reverse('socialAccLogin') + '?' + user_data)
