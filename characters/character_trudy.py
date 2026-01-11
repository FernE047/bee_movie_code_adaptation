from characters.base_character import BaseCharacter
from species.bees import Bee


class Trudy(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Trudy"
        self.nickname = "Trudy"
        self.species = Bee()
