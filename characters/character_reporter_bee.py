from characters.base_character import BaseCharacter
from species.bees import Bee


class ReporterBee(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Reporter Bee", nickname="Reporter Bee", species=Bee())
