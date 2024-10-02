"""This module contains the RequestHelper class for interacting with the Artifacts MMO API."""
import json
import requests


from config import BEARER_TOKEN, TIMEOUT, API_URL #https://api.artifactsmmo.com

class RequestHelper:
    """A helper class for making API requests to the Artifacts MMO API.

    This class provides two static methods for interacting with the API:
    - post_action: For sending POST requests to perform actions on heroes.
    - get_infos: For sending GET requests to retrieve information.

    Both methods handle authentication, URL construction, and error checking internally.

    Raises:
        ValueError: When an invalid HTTP method is specified.
        requests.RequestException: When the API response status code is not 200.

    Note:
        This class uses configuration variables (BEARER_TOKEN, TIMEOUT, API_URL) 
        imported from a config module.
    """
    @staticmethod
    def __make_url(uri: str) -> str:
        return f"{API_URL}{uri}"

    @staticmethod
    def __request(uri: str, method: str, data: dict[str, any] = None) -> list[dict[str, any]]:
        url = RequestHelper.__make_url(uri)
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {BEARER_TOKEN}'
        }
        if method == "POST":
            headers['Content-Type'] = 'application/json'
            response = requests.post(url, headers=headers, data=json.dumps(data), timeout=TIMEOUT)
        elif method == "GET":
            response = requests.get(url, headers=headers, timeout=TIMEOUT)
        else:
            raise ValueError(f"Invalid method: {method}")

        if response.status_code != 200:
            raise requests.RequestException(
                f"Request {url} failed: {response.status_code}, {response.text}"
                )

        data = response.json()
        return data['data']

    @staticmethod
    def __post(uri: str, data: dict[str, any] = None) -> list[dict[str, any]]:
        return RequestHelper.__request(uri, "POST", data)

    @staticmethod
    def __get(uri: str) -> list[dict[str, any]]:
        return RequestHelper.__request(uri, "GET")

    @staticmethod
    def post_action(hero_name: str, action: str, data: dict[str, any]=None) -> list[dict[str, any]]:
        """send a POST request to make an action

        Args:
            hero_name (str): one of your hero name
            action (str): the action verb
                (visit : https://api.artifactsmmo.com/docs for the end point)
            data (dict, optional): the data neded for some request. Defaults to None.

        Returns:
            list: contain the response data
        """
        return RequestHelper.__post(f'/my/{hero_name}/actions/{action}', data)

    @staticmethod
    def get_infos(info: str, subinfos: str='') -> list[dict[str, any]]: 
        """send a GET request to get infos

        Args:
            info (str): The keyword of the info you want
            subinfos (str, optional): The keyword for the infos. Defaults to ''.

        Returns:
            list: contain the response data
        """
        return (RequestHelper.__get(f'/my/{info}/{subinfos}')
                if subinfos != ''
                else RequestHelper.__get(f'/my/{info}'))

print(RequestHelper.get_infos('bank', 'items'))
