from characters.base_character import BaseCharacter
from species.bees import Bee


class Announcer(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Announcer"
        self.nickname = "Announcer"
        self.species = Bee()
