from characters.base_character import BaseCharacter
from species.humans import Human


class AirportSecurity(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Airport Security", nickname="Airport Security", species=Human())