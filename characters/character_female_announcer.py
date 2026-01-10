from characters.base_character import BaseCharacter
from species.humans import Human


class FemaleAnnouncer(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Female announcer"
        self.nickname = "Female announcer"
        self.species = Human()
