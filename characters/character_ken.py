from characters.base_character import BaseCharacter
from species.humans import Human


class Ken(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Ken"
        self.nickname = "Ken"
        self.species = Human()
