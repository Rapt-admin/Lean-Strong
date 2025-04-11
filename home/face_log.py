# face_log.py

import requests
from urllib.parse import urlencode
from django.conf import settings
import jwt
import logging
import urllib.parse


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
        # ##
        # params = {
        #     'client_id': self.client_id,
        #     'redirect_uri': self.redirect_uri,
        #     'scope': 'email,public_profile',
        #     'response_type': 'code',
        #     'state': self._generate_state_token(),
        # }
        # url = f"{self.authorization_url}?{urlencode(params)}"
        # return url, params['state']

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
    #############
        # params = {
        #     'client_id': self.client_id,
        #     'redirect_uri': self.redirect_uri,
        #     'client_secret': self.client_secret,
        #     'code': code,
        # }
        # response = requests.get(self.token_url, params=params)
        # response_data = response.json()
        # logger.debug("Token response data: %s", response_data)
        # if 'error' in response_data:
        #     logger.error("Error in token response: %s", response_data)
        #     raise Exception(f"Error retrieving tokens: {response_data.get('error_description', response_data['error'])}")

        # # Check if 'access_token' is in the response data
        # if 'access_token' not in response_data:
        #     logger.error("Access token not found in response: %s", response_data)
        #     raise KeyError("Access token not found in the response")
        # return FacebookAccessTokens(response_data['access_token'], response_data.get('id_token'))

    def get_user_info(self, access_token):
        user_info_url = "https://graph.facebook.com/me?fields=id,name,email&access_token=" + access_token
        response = requests.get(user_info_url)
        return response.json()
        # params = {
        #     'access_token': access_token,
        # }
        # response = requests.get(self.user_info_url, params=params)
        # return response.json()

    @staticmethod
    def _generate_state_token(length=30):
        from random import SystemRandom
        import string
        return ''.join(SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
