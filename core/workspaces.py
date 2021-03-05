import requests
from . import client
from . import constants

class Workspace(client.Client):

    def get_workspaces(self) -> dict:
        return requests.get(f'{constants.BASE_URL}/workspaces', headers=self.header).json()