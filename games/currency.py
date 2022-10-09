from random import randint
from forex_python.converter import CurrencyRates

from .game_base import Game
from utils import get_value_from_user


class CurrencyRouletteGame(Game):
    def get_money_interval(self, total_amount):
        return total_amount - (5 - self.difficulty), total_amount + (5 - self.difficulty)

    def convert_usd_to_nis(self, usd):
        return

    def get_guess_from_user(self, usd):
        return get_value_from_user(f"how much do you think ${usd} is in NIS", float)

    @staticmethod
    def get_description() -> str:
        return "Currency Roulette - try and guess the value of a random amount of USD in ILS"

    def play(self) -> bool:
        usd = randint(1, 100)
        guess = self.get_guess_from_user(usd)
        currency_rates = CurrencyRates()
        nis = currency_rates.convert('USD', 'ILS', usd)
        intervals = self.get_money_interval(nis)
        return guess in range(intervals[0], intervals[1])
