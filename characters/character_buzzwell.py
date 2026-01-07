from characters.base_character import BaseCharacter
from species.bees import Bee


class Buzzwell(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Buzzwell", nickname="Buzzwell", species=Bee())