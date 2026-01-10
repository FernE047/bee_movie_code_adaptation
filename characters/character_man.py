from characters.base_character import BaseCharacter
from species.humans import Human


class Man(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Man"
        self.nickname = "Man"
        self.species = Human()
