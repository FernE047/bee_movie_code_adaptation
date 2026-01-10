from characters.base_character import BaseCharacter
from species.bees import Bee


class FlightCrewBee(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Flight crew bee"
        self.nickname = "Flight crew bee"
        self.species = Bee()
