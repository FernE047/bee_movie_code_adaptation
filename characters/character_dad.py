from characters.base_character import BaseCharacter
from species.bees import Bee


class Dad(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Dad", nickname="Dad", species=Bee())
