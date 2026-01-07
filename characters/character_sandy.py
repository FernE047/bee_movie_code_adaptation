from characters.base_character import BaseCharacter
from species.bees import Bee


class Sandy(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Sandy Shrimpkin", nickname="Sandy", species=Bee())
