from characters.base_character import BaseCharacter
from species.humans import Human


class Reporter3(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Reporter 3", nickname="Reporter 3", species=Human())
