from characters.base_character import BaseCharacter
from species.humans import Human


class ControlTower(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Control Tower"
        self.nickname = "Control Tower"
        self.species = Human()
