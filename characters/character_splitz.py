from characters.base_character import BaseCharacter
from species.bees import Bee


class Splitz(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Splitz", nickname="Splitz", species=Bee())
