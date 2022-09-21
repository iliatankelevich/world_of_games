from random import randint

from utils import get_value_from_user
from .game_base import Game


class GuessGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.secret_number = None

    def generate_number(self, number: int) -> None:
        self.secret_number = randint(1, number)

    def get_guess_from_user(self, number: int) -> int:
        return get_value_from_user(f"try to guess a number between 1 and {number}", int, lambda x: 1 <= x <= number)

    def compare_results(self, number: int) -> bool:
        return self.secret_number == number

    @staticmethod
    def get_description() -> str:
        return "Guess Game - guess a number and see if you chose like the computer"

    def play(self) -> bool:
        self.generate_number(self.difficulty)
        num_of_tries = 0
        won = False
        while not won:
            num_of_tries += 1
            guess = self.get_guess_from_user(self.difficulty)
            if self.compare_results(guess) and not won:
                print("YEAH!")
                won = True
            else:
                print('nope')
        print(f'congratulations! you guessed after {num_of_tries} tries')
        return True
