from characters.base_character import BaseCharacter
from species.humans import Human


class ControlTower(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Control Tower", nickname="Control Tower", species=Human())