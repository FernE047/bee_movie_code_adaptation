from characters.base_character import BaseCharacter
from species.humans import Human


class Andy(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Andy"
        self.nickname = "Andy"
        self.species = Human()
