from characters.base_character import BaseCharacter
from species.bees import Bee


class Lady1(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Lady 1"
        self.nickname = "Lady 1"
        self.species = Bee()
