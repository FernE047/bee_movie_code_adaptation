from characters.base_character import BaseCharacter
from species.bees import Bee


class Bee1(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Bee 1", nickname="Bee 1", species=Bee())
