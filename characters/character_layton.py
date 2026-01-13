from characters.base_character import BaseCharacter
from species.humans import Human


class Layton(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(
            name="Layton T. Montgomery", nickname="Layton", species=Human()
        )
