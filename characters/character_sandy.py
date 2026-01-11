from characters.base_character import BaseCharacter
from species.bees import Bee


class Sandy(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Sandy Shrimpkin"
        self.nickname = "Sandy"
        self.species = Bee()
