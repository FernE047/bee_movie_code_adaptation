from characters.base_character import BaseCharacter
from species.mosquitoes import Mosquito


class Mooseblood(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Mooseblood"
        self.nickname = "Mooseblood"
        self.species = Mosquito()
