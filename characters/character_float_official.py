from characters.base_character import BaseCharacter
from species.humans import Human


class FloatOfficial(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Float Official"
        self.nickname = "Float Official"
        self.species = Human()
