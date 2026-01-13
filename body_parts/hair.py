from enum import Enum
from body_parts.base_body_parts import BaseBodyPart


class HairType(Enum):
    NONE = "none"
    FUZZ = "fuzz"
    # implement other styles as needed


class Hair(BaseBodyPart):
    def __init__(self) -> None:
        super().__init__("Hair")
        self._type: HairType = HairType.NONE
        self.is_styled = False

    @property
    def type(self) -> HairType:
        return self._type

    @type.setter
    def type(self, value: HairType) -> None:
        self._type = value

    def style_hair(self) -> None:
        self.is_styled = True
