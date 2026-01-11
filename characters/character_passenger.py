from characters.base_character import BaseCharacter
from species.humans import Human


class Passenger(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Passenger"
        self.nickname = "Passenger"
        self.species = Human()
