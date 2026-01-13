from characters.base_character import BaseCharacter
from species.humans import Human


class Reporter2(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Reporter 2", nickname="Reporter 2", species=Human())
