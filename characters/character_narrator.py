from characters.base_character import BaseCharacter
from species.speaker import Speaker


class Narrator(BaseCharacter):
    def __init__(self) -> None:
        self.name = ""
        self.nickname = "Narrator"
        self.species = Speaker()
