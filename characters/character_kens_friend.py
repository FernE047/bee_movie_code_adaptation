from characters.base_character import BaseCharacter
from species.humans import Human


class KensFriend(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Ken's friend"
        self.nickname = "Ken's friend"
        self.species = Human()
