from characters.base_character import BaseCharacter
from species.bees import Bee


class Jackson(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Jackson", nickname="Jackson", species=Bee())
