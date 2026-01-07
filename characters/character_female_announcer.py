from characters.base_character import BaseCharacter
from species.humans import Human


class FemaleAnnouncer(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(
            name="Female announcer", nickname="Female announcer", species=Human()
        )
