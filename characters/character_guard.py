from characters.base_character import BaseCharacter
from species.humans import Human


class Guard(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Guard"
        self.nickname = "Guard"
        self.species = Human()
