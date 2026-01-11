from characters.base_character import BaseCharacter
from species.humans import Human


class Ken(BaseCharacter):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Ken", nickname="Ken", species=Human())
