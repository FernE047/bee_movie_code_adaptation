from characters.base_character import BaseCharacter
from species.base_specie import BaseSpecie


class WaterBug(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Water bug", nickname="Water bug", species=BaseSpecie("Water bug")) #TODO: Implement Water bug specie
