from characters.base_character import BaseCharacter
from species.humans import Human


class Elmo(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Elmo", nickname="Elmo", species=Human())
