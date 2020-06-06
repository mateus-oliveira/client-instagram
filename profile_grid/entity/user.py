class User:
    def __init__(self, id_instagram, username, access_token):
        self.__id_instagram = id_instagram
        self.__username = username
        self.__access_token = access_token

    @property
    def access_token(self):
        return self.__access_token
    @access_token.setter
    def access_token(self, access_token):
        self.__access_token = access_token
        
    @property
    def id_instagram(self):
        return self.__id_instagram
    @id_instagram.setter
    def id_instagram(self, id_instagram):
        self.__id_instagram = id_instagram
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username