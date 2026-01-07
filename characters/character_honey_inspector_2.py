from characters.base_character import BaseCharacter
from species.bees import Bee


class HoneyInspector2(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(
            name="Honey Inspector 2", nickname="Honey Inspector 2", species=Bee()
        )
