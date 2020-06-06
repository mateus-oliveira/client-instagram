 class User:
    def __init__(self, id_instagram, username, accsess_token):
        self.__id_instagram = id_instagram
        self.__username = username
        self.__accsess_token = accsess_token

    @property
    def accsess_token(self):
        return self.__accsess_token
    @accsess_token.setter
    def accsess_token(self, accsess_token):
        self.__accsess_token = accsess_token
        
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