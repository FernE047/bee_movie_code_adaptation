from characters.base_character import BaseCharacter
from species.bees import Bee


class Artie(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Artie", nickname="Artie", species=Bee())