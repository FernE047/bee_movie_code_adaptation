from characters.base_character import BaseCharacter
from species.humans import Human


class Radio(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Radio"
        self.nickname = "Radio"
        self.species = Human()
