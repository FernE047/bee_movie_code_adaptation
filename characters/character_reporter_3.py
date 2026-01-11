from characters.base_character import BaseCharacter
from species.humans import Human


class Reporter3(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Reporter 3"
        self.nickname = "Reporter 3"
        self.species = Human()
