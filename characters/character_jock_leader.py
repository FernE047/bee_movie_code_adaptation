from characters.base_character import BaseCharacter
from species.bees import Bee


class JockLeader(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Jock Leader"
        self.nickname = "Jock Leader"
        self.species = Bee()
