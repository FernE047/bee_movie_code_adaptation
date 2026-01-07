from characters.base_character import BaseCharacter
from species.speaker import Speaker


class Narrator(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="", nickname="Narrator", species=Speaker())
