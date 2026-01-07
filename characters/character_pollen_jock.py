from characters.base_character import BaseCharacter
from species.bees import Bee


class PollenJock(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Pollen Jock", nickname="Pollen Jock", species=Bee())
