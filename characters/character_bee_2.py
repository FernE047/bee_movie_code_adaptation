from characters.base_character import BaseCharacter
from species.bees import Bee


class Bee2(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Bee 2", nickname="Bee 2", species=Bee())
