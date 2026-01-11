from characters.base_character import BaseCharacter
from species.humans import Human


class FloatOfficial(BaseCharacter):
    species: Human

    def __init__(self) -> None:
        super().__init__(
            name="Float Official", nickname="Float Official", species=Human()
        )
