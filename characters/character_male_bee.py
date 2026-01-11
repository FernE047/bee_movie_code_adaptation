from characters.base_character import BaseCharacter
from species.bees import Bee


class MaleBee(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Male bee"
        self.nickname = "Male bee"
        self.species = Bee()
