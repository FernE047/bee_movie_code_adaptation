from characters.base_character import BaseCharacter
from species.bees import Bee


class TestingBee2(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Testing bee 2"
        self.nickname = "Testing bee 2"
        self.species = Bee()
