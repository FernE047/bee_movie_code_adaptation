from characters.base_character import BaseCharacter
from species.bees import Bee


class PollenJock(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Pollen Jock"
        self.nickname = "Pollen Jock"
        self.species = Bee()
