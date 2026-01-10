from characters.base_character import BaseCharacter
from species.humans import Human


class Janitor(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Janitor"
        self.nickname = "Janitor"
        self.species = Human()
