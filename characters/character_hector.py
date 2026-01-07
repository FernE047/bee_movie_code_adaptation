from characters.base_character import BaseCharacter
from species.humans import Human


class Hector(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Hector", nickname="Hector", species=Human())
