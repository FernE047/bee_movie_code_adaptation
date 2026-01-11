from characters.base_character import BaseCharacter
from species.bears import Bear


class BearCharacter(BaseCharacter):
    species: Bear

    def __init__(self) -> None:
        super().__init__(name="Bear", nickname="Bear", species=Bear())
