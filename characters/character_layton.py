from characters.base_character import BaseCharacter
from species.humans import Human


class Layton(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Layton T. Montgomery"
        self.nickname = "Layton"
        self.species = Human()
