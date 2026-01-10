from characters.base_character import BaseCharacter
from species.humans import Human


class Reporter1(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Reporter 1"
        self.nickname = "Reporter 1"
        self.species = Human()
