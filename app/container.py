from yaml import safe_load


class Container:
    def __init__(self):
        #F:/delivery/deliveryBackend/AuthService/config.yml
        #D:/delivery/backend/AuthService/config.yml
        self.__data = safe_load(open('F:/delivery/deliveryBackend/AuthService/config.yml', 'r'))
        self.__db = self.__data["db"]
        self.__auth = self.__data["auth"]

    def get_auth(self):
        return self.__auth

    def get_db(self):
        return self.__db

    db = property(get_db)
    auth = property(get_auth)
