from characters.base_character import BaseCharacter
from species.bees import Bee


class Artie(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Artie", nickname="Artie", species=Bee())
