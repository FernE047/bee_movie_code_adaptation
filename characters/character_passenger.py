from characters.base_character import BaseCharacter
from species.humans import Human


class Passenger(BaseCharacter):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Passenger", nickname="Passenger", species=Human())
