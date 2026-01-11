from characters.base_character import BaseCharacter
from species.bees import Bee


class Jackson(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Jackson"
        self.nickname = "Jackson"
        self.species = Bee()
