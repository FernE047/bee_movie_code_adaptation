from characters.base_character import BaseCharacter
from species.humans import Human


class Guard(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Guard", nickname="Guard", species=Human())
