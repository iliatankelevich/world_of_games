import time
from random import randint

from utils import get_value_from_user, is_list_equal, screen_clear
from .game_base import Game


class MemoryGame(Game):
    def generate_sequence(self):
        sequence = []
        for i in range(self.difficulty):
            sequence.append(randint(1, 101))
        return sequence

    def get_list_from_user(self):
        sequence_from_user = []
        for i in range(self.difficulty):
            sequence_from_user.append(get_value_from_user(f"type #{i} number", int, lambda x: 1 <= x <= 101))

        return sequence_from_user

    @staticmethod
    def get_description() -> str:
        return "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"

    def play(self) -> bool:
        generated_sequence = self.generate_sequence()
        print(generated_sequence)
        time.sleep(7)
        screen_clear()
        sequence_from_user = self.get_list_from_user()
        return is_list_equal(generated_sequence, sequence_from_user)
