from characters.base_character import BaseCharacter
from species.bees import Bee


class Bee2(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Bee 2"
        self.nickname = "Bee 2"
        self.species = Bee()
