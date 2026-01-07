from characters.base_character import BaseCharacter
from species.bees import Bee


class ControlRoomBee(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Control Room Bee", nickname="Control Room Bee", species=Bee())