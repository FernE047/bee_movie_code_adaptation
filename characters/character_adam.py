from characters.base_character import BaseCharacter
from species.bees import Bee


class Adam(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Adam", nickname="Adam", species=Bee())
