from characters.base_character import BaseCharacter
from species.bees import Bee


class CameramanBee(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Cameraman Bee", nickname="Cameraman Bee", species=Bee())
