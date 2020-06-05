# coding: utf-8

from social_core.backends.oauth import BaseOAuth2
from profile_grid.models import User


class InstagramOAuth2(BaseOAuth2):
    name = 'instagram'
    AUTHORIZATION_URL = 'https://api.instagram.com/oauth/authorize'
    ACCESS_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = False
    STATE_PARAMETER = False
    USER_DATA_URL = 'https://graph.instagram.com/me/media'
    

    def user_data(self, access_token, *args, **kwargs):
        print('here', access_token, *args, **kwargs)
        return self.request(
            url=self.USER_DATA_URL,
            method='GET',
        ).json()


    def get_user_details(self, response):
        
        print("response", response)
        
        # usuario, criado = Usuario.objects.get_or_create(
        #     identificacao = response["identificacao"],
        #     nome = response["nome"],
        #     email = response["email"],
        #     campus = response["campus"],
        # )

        return response
