from characters.base_character import BaseCharacter
from species.speaker import Speaker


class Narrator(BaseCharacter[Speaker]):
    species: Speaker

    def __init__(self) -> None:
        super().__init__(name="", nickname="Narrator", species=Speaker())
