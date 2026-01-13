from characters.base_character import BaseCharacter
from species.bees import Bee


class MaleBee(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Male bee", nickname="Male bee", species=Bee())
