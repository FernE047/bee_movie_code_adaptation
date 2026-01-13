from characters.base_character import BaseCharacter
from species.humans import Human


class YoungGirl(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Young girl", nickname="Young girl", species=Human())
