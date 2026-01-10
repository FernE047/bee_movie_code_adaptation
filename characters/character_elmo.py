from characters.base_character import BaseCharacter
from species.humans import Human


class Elmo(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Elmo"
        self.nickname = "Elmo"
        self.species = Human()
