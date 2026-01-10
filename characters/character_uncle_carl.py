from characters.base_character import BaseCharacter
from species.bees import Bee


class UncleCarl(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Uncle Carl"
        self.nickname = "Uncle Carl"
        self.species = Bee()
