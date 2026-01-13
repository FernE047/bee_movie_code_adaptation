from characters.base_character import BaseCharacter
from species.humans import Human


class Hal(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Hal", nickname="Hal", species=Human())
