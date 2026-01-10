from __future__ import annotations
from typing import TYPE_CHECKING
from body_parts.bee_phone import BeePhone
from species.base_specie import BaseSpecie

if TYPE_CHECKING:
    from characters.base_character import BaseCharacter


class Bee(BaseSpecie):
    def __init__(self) -> None:
        self.name = "Bee"
        self.can_fly_flag = True
        self.should_fly = False
        self.bee_phone = BeePhone(ringtone="Bzzzt Bzzt")

    def receive_call(self, caller: BaseCharacter, owner: BaseCharacter) -> None:
        self.bee_phone.set_owner(owner)
        self.bee_phone.rings(caller)

    def answers(self) -> None:
        self.bee_phone.answers()

    def hangs_up(self) -> None:
        self.bee_phone.hangs_up()
