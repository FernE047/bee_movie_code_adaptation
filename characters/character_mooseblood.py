from characters.base_character import BaseCharacter
from species.mosquitoes import Mosquito


class Mooseblood(BaseCharacter[Mosquito]):
    species: Mosquito

    def __init__(self) -> None:
        super().__init__(name="Mooseblood", nickname="Mooseblood", species=Mosquito())
