from characters.base_character import BaseCharacter
from species.humans import Human


class Radio(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Radio", nickname="Radio", species=Human())
