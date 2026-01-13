from characters.base_character import BaseCharacter
from species.bees import Bee


class UncleCarl(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Uncle Carl", nickname="Uncle Carl", species=Bee())
