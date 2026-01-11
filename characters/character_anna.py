from characters.base_character import BaseCharacter
from species.humans import Human


class Anna(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Anna"
        self.nickname = "Anna"
        self.species = Human()
