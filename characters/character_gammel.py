from characters.base_character import BaseCharacter
from species.humans import Human


class Gammel(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Gammel"
        self.nickname = "Gammel"
        self.species = Human()
