from characters.base_character import BaseCharacter
from species.humans import Human


class Driver(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Driver", nickname="Driver", species=Human())