from characters.base_character import BaseCharacter
from species.bees import Bee


class Grandma(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Grandma", nickname="Grandma", species=Bee())
