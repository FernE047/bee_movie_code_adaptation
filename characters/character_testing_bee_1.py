from characters.base_character import BaseCharacter
from species.bees import Bee


class TestingBee1(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Testing bee 1", nickname="Testing bee 1", species=Bee())
