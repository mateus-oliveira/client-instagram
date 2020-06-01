 
class User:
    def __init__(self, id_instagram, username, token):
        self.__id_instagram = id_instagram
        self.__username = username
        self.__token = token

    @property
    def token(self):
        return self.__token
    @token.setter
    def token(self, token):
        self.__token = token
        
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