import requests
from . import constants


class MissingApiKeyError(Exception):
    pass


class Client:
    def __init__(self, api_key: str):
        try:
            self.header = {"X-Api-Key": api_key}
        except:
            raise MissingApiKeyError(
                "No API Key Provided. Please provide one when instantiating the Client class.")

    def get_current_user(self) -> dict:
        return requests.get(f'{constants.BASE_URL}/user', headers=self.header).json()
