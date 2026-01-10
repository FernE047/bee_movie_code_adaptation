from characters.base_character import BaseCharacter
from species.humans import Human


class Father(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Father"
        self.nickname = "Father"
        self.species = Human()
