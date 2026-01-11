from characters.base_character import BaseCharacter
from species.bees import Bee


class ControlRoomBee(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Control Room Bee"
        self.nickname = "Control Room Bee"
        self.species = Bee()
