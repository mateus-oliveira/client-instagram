# coding: utf-8

from social_core.backends.oauth import BaseOAuth2
from profile_grid.services.user_service import *
from profile_grid.entity.user import User

import json


class InstagramOAuth2(BaseOAuth2):
    name = 'instagram'
    AUTHORIZATION_URL = 'https://api.instagram.com/oauth/authorize'
    ACCESS_TOKEN_METHOD = 'POST'
    ID_KEY = 'user_id'
    ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = False
    STATE_PARAMETER = False
    USER_MEDIA_URL = 'https://graph.instagram.com/me/media' 
    USER_DATA_URL = "https://graph.instagram.com/" 

    def user_data(self, access_token, *args, **kwargs):
        return self.request(
            url="{}{}".format(self.USER_DATA_URL, kwargs['response']['user_id']),
            method='GET',
            params={
                "fields": "id,username,account_type",
                "access_token": access_token,
            }
        ).json()

    def get_user_details(self, response):
        # print(json.dumps(
        #     response,
        #     sort_keys=True,
        #     indent=4,
        #     separators=(',', ': '),
        # ))

        new_user = User(
            id_instagram=response[self.ID_KEY],
            username=response['username'],
            access_token=response["access_token"],
        )

        user = find_user(new_user.id_instagram)

        if user == None:
            create_user(new_user)
        else:
            update_user(user, new_user)

        return {
            'username': str(response["username"]),
            'first_name': str(response["username"]),
        } # Tabela auth_user
