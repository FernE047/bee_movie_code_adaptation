from characters.base_character import BaseCharacter
from species.humans import Human


class Judge(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Judge"
        self.nickname = "Judge"
        self.species = Human()
