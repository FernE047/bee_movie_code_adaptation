from characters.base_character import BaseCharacter
from species.bees import Bee


class Jeanette(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Jeanette Chung"
        self.nickname = "Jeanette"
        self.species = Bee()
