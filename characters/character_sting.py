from characters.base_character import BaseCharacter
from species.bees import Bee


class Sting(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Sting"
        self.nickname = "Sting"
        self.species = Bee()
