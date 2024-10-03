"""Module providing a class to instance a character."""

from typing import Dict, List, Any
from request_helper import RequestHelper

class Hero:
    """Character base class.

    This class can be extand.

    Attributes:
        name (string): The name of the character the player want to play.

    Methods:
        methode1(param1, param2): Brève description de methode1.
        methode2(param): Brève description de methode2.
    """
    def __init__(self, name: str):
        """Init of Character.

        Args:
            name (string): The name of the character the player want to play.
        """
        self.name = name

    def move_to(self, content_code: str):
        """Move the hero

        Args:
            content_code (_string_): Match pattern: ^[a-zA-Z0-9_-]+$

        Returns:
            _type_: _description_
        """
        return self.make_action(
            'move',
            RequestHelper.get_map_tile_coord(content_code)
            )

    def make_action(self, action: str,  data: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Perform an action with this Hero

        Args:
            action (str): The action verb
            data (Dict[str, Any], optional): some data if needed. Defaults to None.

        Returns:
            List[Dict[str, Any]]: The response data
        """
        return RequestHelper.post_action(self.name, action, data)

    def search_infos(self, first_info: str, second_info: str = '') -> List[Dict[str, Any]]:
        """search for some infos on this hero

        Args:
            first_info (str): can be :
            -logs
            -characters
            -bank
            second_info (str): can only be 'items' when first_info is 'bank'

        Returns:
            List[Dict[str, Any]]: The response data
        """
        return RequestHelper.get_infos(first_info, second_info)
