from characters.base_character import BaseCharacter
from species.bees import Bee


class CameramanBee(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Cameraman Bee"
        self.nickname = "Cameraman Bee"
        self.species = Bee()
