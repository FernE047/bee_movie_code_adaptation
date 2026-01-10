from characters.base_character import BaseCharacter
from species.bees import Bee


class Splitz(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Splitz"
        self.nickname = "Splitz"
        self.species = Bee()
