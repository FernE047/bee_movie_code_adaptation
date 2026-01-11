from characters.base_character import BaseCharacter
from species.bees import Bee


class JockLeader(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Jock Leader", nickname="Jock Leader", species=Bee())
