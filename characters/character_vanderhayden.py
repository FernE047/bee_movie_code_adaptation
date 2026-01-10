from characters.base_character import BaseCharacter
from species.humans import Human


class Vanderhayden(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Vanderhayden"
        self.nickname = "Vanderhayden"
        self.species = Human()
