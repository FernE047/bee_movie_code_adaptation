from characters.base_character import BaseCharacter
from species.humans import Human


class YoungGirl(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Young girl"
        self.nickname = "Young girl"
        self.species = Human()
