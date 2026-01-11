from characters.base_character import BaseCharacter
from species.bees import Bee


class Lady2(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Lady 2"
        self.nickname = "Lady 2"
        self.species = Bee()
