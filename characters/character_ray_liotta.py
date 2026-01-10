from characters.base_character import BaseCharacter
from species.humans import Human


class RayLiotta(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Ray Liotta"
        self.nickname = "Ray Liotta"
        self.species = Human()
