from characters.base_character import BaseCharacter
from species.bees import Bee


class Jeanette(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Jeanette Chung", nickname="Jeanette", species=Bee())
