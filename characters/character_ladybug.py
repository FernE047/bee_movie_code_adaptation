from characters.base_character import BaseCharacter
from species.base_specie import BaseSpecie


class Ladybug(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Ladybug", nickname="Ladybug", species=BaseSpecie("Ladybug")) #TODO: Implement Ladybug species
