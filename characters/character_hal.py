from characters.base_character import BaseCharacter
from species.humans import Human


class Hal(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Hal"
        self.nickname = "Hal"
        self.species = Human()
