from characters.base_character import BaseCharacter
from species.humans import Human


class TheFloatPrincess(BaseCharacter):
    def __init__(self) -> None:
        self.name = "The Float Princess"
        self.nickname = "The Float Princess"
        self.species = Human()
