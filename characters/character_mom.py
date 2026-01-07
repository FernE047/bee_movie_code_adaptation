from characters.base_character import BaseCharacter
from species.bees import Bee


class Mom(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Mom", nickname="Mom", species=Bee())
