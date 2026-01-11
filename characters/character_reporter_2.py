from characters.base_character import BaseCharacter
from species.humans import Human


class Reporter2(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Reporter 2"
        self.nickname = "Reporter 2"
        self.species = Human()
