from .game_base import Game


class MemoryGame(Game):
    @staticmethod
    def get_description() -> str:
        return "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"

    def play(self) -> bool:
        pass
