from characters.base_character import BaseCharacter
from species.humans import Human


class Judge(BaseCharacter):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Judge", nickname="Judge", species=Human())
