from characters.base_character import BaseCharacter
from species.bees import Bee


class Bob(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Bob Bumble"
        self.nickname = "Bob"
        self.species = Bee()