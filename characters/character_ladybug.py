from characters.base_character import BaseCharacter
from species.ladybugs import Ladybug


class LadybugCharacter(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Ladybug"
        self.nickname = "Ladybug"
        self.species = Ladybug()
