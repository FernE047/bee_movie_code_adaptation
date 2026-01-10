from characters.base_character import BaseCharacter
from species.humans import Human


class AtfhAgent(BaseCharacter):
    def __init__(self) -> None:
        self.name = "ATFH Agent"
        self.nickname = "ATFH Agent"
        self.species = Human()
