"""The application controller"""
from hero import Hero

class ApplicationController:
    """Main controller, called when the app start"""

    def __init__(self):
        self.controller = None

    def start(self):
        """define your gameplay loop here"""
        hero = Hero('Darwin')
        while True:
            hero.move_to('ash_tree')
            for i in range(80):
                hero.make_action('gathering')
            hero.move_to('woodcutting')
            hero.make_action('crafting', {'code': 'ash_plank', 'quantity':10})
            hero.move_to('bank')
            hero.make_action('bank/deposit', {"code": "ash_plank", "quantity": 10})
