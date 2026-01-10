from characters.base_character import BaseCharacter
from species.speaker import Speaker


class Narrator(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Narrator", nickname="Narrator", species=Speaker())
        self.name = ""
        self.nickname = "Narrator"
        self.species = Speaker()
