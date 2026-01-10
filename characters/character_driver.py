from characters.base_character import BaseCharacter
from species.humans import Human


class Driver(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Driver"
        self.nickname = "Driver"
        self.species = Human()
