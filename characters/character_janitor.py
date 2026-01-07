from characters.base_character import BaseCharacter
from species.humans import Human


class Janitor(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Janitor", nickname="Janitor", species=Human())
