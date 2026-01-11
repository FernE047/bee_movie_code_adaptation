from characters.base_character import BaseCharacter
from species.humans import Human


class YoungBoy(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Young boy"
        self.nickname = "Young boy"
        self.species = Human()
