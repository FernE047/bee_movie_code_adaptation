from characters.base_character import BaseCharacter
from species.bees import Bee


class Trudy(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Trudy", nickname="Trudy", species=Bee())
