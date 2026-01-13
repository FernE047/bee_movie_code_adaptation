from characters.base_character import BaseCharacter
from species.bees import Bee


class Lady2(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Lady 2", nickname="Lady 2", species=Bee())
