from characters.base_character import BaseCharacter
from species.humans import Human


class Reporter1(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Reporter 1", nickname="Reporter 1", species=Human())
