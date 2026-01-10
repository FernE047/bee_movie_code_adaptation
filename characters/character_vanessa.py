from characters.base_character import BaseCharacter
from species.humans import Human


class Vanessa(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Vanessa"
        self.nickname = "Vanessa"
        self.species = Human()
