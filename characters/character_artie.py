from characters.base_character import BaseCharacter
from species.bees import Bee


class Artie(BaseCharacter):
    def __init__(self) -> None:
        
        self.name="Artie"
        self.nickname="Artie"
        self.species=Bee()