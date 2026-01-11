from characters.base_character import BaseCharacter
from species.humans import Human


class Bailiff(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Bailiff"
        self.nickname = "Bailiff"
        self.species = Human()
