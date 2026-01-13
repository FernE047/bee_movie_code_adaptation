from characters.base_character import BaseCharacter
from species.humans import Human


class Father(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Father", nickname="Father", species=Human())
