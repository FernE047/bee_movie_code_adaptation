from characters.base_character import BaseCharacter
from species.bees import Bee


class Sting(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Sting", nickname="Sting", species=Bee())
