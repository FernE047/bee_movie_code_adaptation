from characters.base_character import BaseCharacter
from species.humans import Human


class Andy(BaseCharacter):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Andy", nickname="Andy", species=Human())
