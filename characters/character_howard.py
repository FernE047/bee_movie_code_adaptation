from characters.base_character import BaseCharacter
from species.bees import Bee


class Howard(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Howard"
        self.nickname = "Howard"
        self.species = Bee()
