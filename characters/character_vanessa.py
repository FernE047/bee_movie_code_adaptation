from characters.base_character import BaseCharacter
from species.humans import Human


class Vanessa(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Vanessa", nickname="Vanessa", species=Human())
