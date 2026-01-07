from characters.base_character import BaseCharacter
from species.bees import Bee


class HoneyInspector1(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(
            name="Honey Inspector 1", nickname="Honey Inspector 1", species=Bee()
        )
