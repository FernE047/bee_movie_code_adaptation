from characters.base_character import BaseCharacter
from species.bears import Bear


class BearCharacter(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Bear"
        self.nickname = "Bear"
        self.species = Bear()
