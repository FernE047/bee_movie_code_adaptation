from characters.base_character import BaseCharacter
from species.humans import Human


class Captain(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Captain Scott", nickname="Captain", species=Human())