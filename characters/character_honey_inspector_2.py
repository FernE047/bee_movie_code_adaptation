from characters.base_character import BaseCharacter
from species.bees import Bee


class HoneyInspector2(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Honey Inspector 2"
        self.nickname = "Honey Inspector 2"
        self.species = Bee()
