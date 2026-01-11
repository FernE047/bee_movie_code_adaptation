from characters.base_character import BaseCharacter
from species.bees import Bee


class Lady1(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Lady 1", nickname="Lady 1", species=Bee())
