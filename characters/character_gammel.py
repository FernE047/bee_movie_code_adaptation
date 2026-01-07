from characters.base_character import BaseCharacter
from species.humans import Human


class Gammel(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Gammel", nickname="Gammel", species=Human())