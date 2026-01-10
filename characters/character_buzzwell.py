from characters.base_character import BaseCharacter
from species.bees import Bee


class Buzzwell(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Buzzwell"
        self.nickname = "Buzzwell"
        self.species = Bee()
