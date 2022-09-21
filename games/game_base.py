from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    @staticmethod
    @abstractmethod
    def get_description() -> str:
        pass

    @abstractmethod
    def play(self) -> bool:
        pass
