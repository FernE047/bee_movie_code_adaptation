from __future__ import annotations
from typing import TYPE_CHECKING
from body_parts.antenna import Antenna
from species.base_specie import BaseSpecie

if TYPE_CHECKING:
    from characters.base_character import BaseCharacter


class Bee(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Bee", can_fly=True, should_fly=False)
        self.antenna = Antenna(ringtone="Bzzzt")

    def receive_call(self, caller: BaseCharacter, owner: BaseCharacter) -> None:
        self.antenna.set_owner(owner)
        self.antenna.rings(caller)

    def answers(self) -> None:
        self.antenna.answers()

    def hangs_up(self) -> None:
        self.antenna.hangs_up()
