from games.currency import CurrencyRouletteGame
from games.memory import MemoryGame
from games.guess import GuessGame
from utils import get_value_from_user


class Live:
    def __init__(self):
        self.games = (MemoryGame, GuessGame, CurrencyRouletteGame)

    @staticmethod
    def welcome(name: str) -> str:
        return f'hello {name} and welcome to the World of Games (WOG). \n Here you can find many cool games to play'

    def load_games(self):
        while True:
            print('Please choose a game to play:')
            exit_index = len(self.games) + 1
            for game in self.games:
                print(f'{self.games.index(game) + 1}. {game.get_description()}')
            print(f'{len(self.games) + 1}. exit')
            menu_index = get_value_from_user('which game would you like to play:', int, lambda index: 1 <= index <= exit_index)
            if menu_index == exit_index:
                break
            game_index = menu_index - 1
            difficulty = get_value_from_user('please choose the level of difficulty from 1 to 5', int, lambda index: 1 <= index <= 5)
            game = self.games[game_index]
            initiated_game = game(difficulty)
            initiated_game.play()

        print('goodbye')
