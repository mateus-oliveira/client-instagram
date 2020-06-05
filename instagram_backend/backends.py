# coding: utf-8

from social_core.backends.oauth import BaseOAuth2
from profile_grid.models import User

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
    USER_DATA_URL = 'https://graph.instagram.com/me/media'  


    def user_data(self, access_token, *args, **kwargs):
        return self.request(
            url=self.USER_DATA_URL,
            method='GET',
            params={
                "fields": "id,media_type,media_url,username,timestamp",
                "access_token": access_token,
            }
        ).json()


    def get_user_details(self, response):
        print(json.dumps(
            response,
            sort_keys=True,
            indent=4,
            separators=(',', ': '),
        ))

        return {
            "id": response[self.ID_KEY]
        }
