from characters.base_character import BaseCharacter
from species.humans import Human


class AtfhAgent(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="ATFH Agent", nickname="ATFH Agent", species=Human())