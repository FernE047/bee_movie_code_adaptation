from characters.base_character import BaseCharacter
from species.humans import Human


class KidWithAFrisbee(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(
            name="Kid with a frisbee", nickname="Kid with a frisbee", species=Human()
        )
