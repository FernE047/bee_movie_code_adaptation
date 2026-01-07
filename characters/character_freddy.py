from characters.base_character import BaseCharacter
from species.humans import Human


class Freddy(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Freddy", nickname="Freddy", species=Human())