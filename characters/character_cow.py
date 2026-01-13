from characters.base_character import BaseCharacter
from species.cow import Cow


class CowCharacter(BaseCharacter[Cow]):
    species: Cow

    def __init__(self) -> None:
        super().__init__(name="Cow", nickname="Cow", species=Cow())
