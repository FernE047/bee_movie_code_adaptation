from characters.base_character import BaseCharacter
from species.ladybugs import Ladybug


class LadybugCharacter(BaseCharacter[Ladybug]):
    species: Ladybug

    def __init__(self) -> None:
        super().__init__(name="Ladybug", nickname="Ladybug", species=Ladybug())
