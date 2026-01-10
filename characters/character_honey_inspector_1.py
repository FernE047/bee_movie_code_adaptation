from characters.base_character import BaseCharacter
from species.bees import Bee


class HoneyInspector1(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Honey Inspector 1"
        self.nickname = "Honey Inspector 1"
        self.species = Bee()
