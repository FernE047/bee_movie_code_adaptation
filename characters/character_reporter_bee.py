from characters.base_character import BaseCharacter
from species.bees import Bee


class ReporterBee(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Reporter Bee"
        self.nickname = "Reporter Bee"
        self.species = Bee()
