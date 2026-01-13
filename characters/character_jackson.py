from characters.base_character import BaseCharacter
from species.bees import Bee


class Jackson(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Jackson", nickname="Jackson", species=Bee())
