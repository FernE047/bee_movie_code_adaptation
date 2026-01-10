from characters.base_character import BaseCharacter
from species.humans import Human


class Captain(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Captain Scott"
        self.nickname = "Captain"
        self.species = Human()
