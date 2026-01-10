from characters.base_character import BaseCharacter
from species.bees import Bee


class Adam(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Adam", nickname="Adam", species=Bee())
        self.name = "Adam"
        self.nickname = "Adam"
        self.species = Bee()
