class LoginInfo:
    def __init__(self, access_token, instance_url, token_type):
        self.__access_token = access_token
        self.__instance_url = instance_url
        self.__token_type = token_type

    def getAccessToken(self):
        return self.__access_token

    def getInstanceUrl(self):
        return self.__instance_url

    def getTokenType(self):
        return self.__token_type
