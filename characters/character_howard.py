from characters.base_character import BaseCharacter
from species.bees import Bee


class Howard(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Howard", nickname="Howard", species=Bee())
