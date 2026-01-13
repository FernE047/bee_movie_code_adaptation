from characters.base_character import BaseCharacter
from species.bees import Bee


class Bob(BaseCharacter[Bee]):
    species: Bee

    def __init__(self) -> None:
        super().__init__(name="Bob Bumble", nickname="Bob", species=Bee())
