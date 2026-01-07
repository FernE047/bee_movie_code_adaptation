from characters.base_character import BaseCharacter
from species.base_specie import BaseSpecie


class Bear(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(
            name="Bear", nickname="Bear", species=BaseSpecie("Bear")
        )  # TODO: implement Bears
