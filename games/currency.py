from .game_base import Game


class CurrencyRouletteGame(Game):
    @staticmethod
    def get_description() -> str:
        return "Currency Roulette - try and guess the value of a random amount of USD in ILS"

    def play(self) -> bool:
        pass
