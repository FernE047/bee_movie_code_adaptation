from characters.base_character import BaseCharacter
from species.bees import Bee


class TestingBee1(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Testing bee 1"
        self.nickname = "Testing bee 1"
        self.species = Bee()
