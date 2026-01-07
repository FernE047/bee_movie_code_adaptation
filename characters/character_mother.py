from characters.base_character import BaseCharacter
from species.humans import Human


class Mother(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Mother", nickname="Mother", species=Human())
