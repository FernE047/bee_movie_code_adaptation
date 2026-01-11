from characters.base_character import BaseCharacter
from species.bees import Bee


class TestingBee2(BaseCharacter):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Testing bee 2", nickname="Testing bee 2", species=Bee())
