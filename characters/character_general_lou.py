from characters.base_character import BaseCharacter
from species.bees import Bee


class GeneralLou(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="General Lou", nickname="General", species=Bee())