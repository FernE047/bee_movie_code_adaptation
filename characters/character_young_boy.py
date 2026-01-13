from characters.base_character import BaseCharacter
from species.humans import Human


class YoungBoy(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Young boy", nickname="Young boy", species=Human())
