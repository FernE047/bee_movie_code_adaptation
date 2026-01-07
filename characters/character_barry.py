from characters.base_character import BaseCharacter
from species.bees import Bee


class Barry(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Barry", nickname="Barry", species=Bee())