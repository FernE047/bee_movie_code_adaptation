from characters.base_character import BaseCharacter
from species.humans import Human


class KensFriend(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(name="Ken's friend", nickname="Ken's friend", species=Human())
