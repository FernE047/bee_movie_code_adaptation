from characters.base_character import BaseCharacter
from species.bees import Bee


class Bee1(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Bee 1"
        self.nickname = "Bee 1"
        self.species = Bee()
