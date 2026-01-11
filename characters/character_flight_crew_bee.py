from characters.base_character import BaseCharacter
from species.bees import Bee


class FlightCrewBee(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(
            name="Flight crew bee", nickname="Flight crew bee", species=Bee()
        )
