from characters.base_character import BaseCharacter
from species.bees import Bee


class BeeLarryKing(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Bee Larry King"
        self.nickname = "Bee Larry King"
        self.species = Bee()
