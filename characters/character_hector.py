from characters.base_character import BaseCharacter
from species.humans import Human


class Hector(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Hector"
        self.nickname = "Hector"
        self.species = Human()
