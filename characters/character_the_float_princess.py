from characters.base_character import BaseCharacter
from species.humans import Human


class TheFloatPrincess(BaseCharacter[Human]):
    species: Human

    def __init__(self) -> None:
        super().__init__(
            name="The Float Princess", nickname="The Float Princess", species=Human()
        )
