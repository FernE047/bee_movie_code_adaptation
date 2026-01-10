from characters.base_character import BaseCharacter
from species.waterbugs import WaterBug


class WaterBugCharacter(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Water bug"
        self.nickname = "Water bug"
        self.species = WaterBug()
