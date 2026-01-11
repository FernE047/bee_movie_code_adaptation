from characters.base_character import BaseCharacter
from species.humans import Human


class RayLiotta(BaseCharacter):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Ray Liotta", nickname="Ray Liotta", species=Human())
