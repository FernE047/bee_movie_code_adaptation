from characters.base_character import BaseCharacter
from species.humans import Human


class Man(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Man", nickname="Man", species=Human())
