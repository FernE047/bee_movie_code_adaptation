from characters.base_character import BaseCharacter
from species.bees import Bee


class GeneralLou(BaseCharacter):
    def __init__(self) -> None:
        self.name = "General Lou"
        self.nickname = "General"
        self.species = Bee()
