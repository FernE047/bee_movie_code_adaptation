from characters.base_character import BaseCharacter
from species.humans import Human


class Anna(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Anna", nickname="Anna", species=Human())
