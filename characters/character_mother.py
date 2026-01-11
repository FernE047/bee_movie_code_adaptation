from characters.base_character import BaseCharacter
from species.humans import Human


class Mother(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Mother"
        self.nickname = "Mother"
        self.species = Human()
