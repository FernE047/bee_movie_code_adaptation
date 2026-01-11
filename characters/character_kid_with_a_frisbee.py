from characters.base_character import BaseCharacter
from species.humans import Human


class KidWithAFrisbee(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Kid with a frisbee"
        self.nickname = "Kid with a frisbee"
        self.species = Human()
