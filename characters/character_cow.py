from characters.base_character import BaseCharacter
from species.cow import Cow


class CowCharacter(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Cow"
        self.nickname = "Cow"
        self.species = Cow()
