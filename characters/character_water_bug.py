from characters.base_character import BaseCharacter
from species.waterbugs import WaterBug


class WaterBugCharacter(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Water bug", nickname="Water bug", species=WaterBug())
