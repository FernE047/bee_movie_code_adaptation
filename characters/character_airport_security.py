from characters.base_character import BaseCharacter
from species.humans import Human


class AirportSecurity(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Airport Security"
        self.nickname = "Airport Security"
        self.species = Human()
