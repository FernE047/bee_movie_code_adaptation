from characters.base_character import BaseCharacter
from species.humans import Human


class MrDitchwater(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Mr Ditchwater"
        self.nickname = "Mr Ditchwater"
        self.species = Human()
