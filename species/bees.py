from __future__ import annotations
from typing import TYPE_CHECKING
from body_parts.antenna import Antenna
from body_parts.hair import HairType
from species.base_specie import BaseSpecie, WeightDescriptions

if TYPE_CHECKING:
    from characters.base_character import BaseCharacter


class Bee(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Bee", weight=WeightDescriptions.FAT, has_wings=True)
        self.antenna = Antenna(ringtone="Bzzzt")
        self.hair.type = HairType.FUZZ
        self.add_body_part(self.antenna)

    def receive_call(
        self, caller: BaseCharacter[Bee], owner: BaseCharacter[Bee]
    ) -> None:
        self.antenna.set_owner(owner)
        self.antenna.rings(caller)

    def answers(self) -> None:
        self.antenna.answers()

    def hangs_up(self) -> None:
        self.antenna.hangs_up()
