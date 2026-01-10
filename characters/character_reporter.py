from characters.base_character import BaseCharacter
from species.humans import Human


class Reporter(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Reporter"
        self.nickname = "Reporter"
        self.species = Human()
