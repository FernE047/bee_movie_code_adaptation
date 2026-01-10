from characters.base_character import BaseCharacter
from species.bees import Bee


class Dad(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Dad"
        self.nickname = "Dad"
        self.species = Bee()
