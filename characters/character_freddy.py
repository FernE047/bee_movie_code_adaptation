from characters.base_character import BaseCharacter
from species.humans import Human


class Freddy(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Freddy"
        self.nickname = "Freddy"
        self.species = Human()
