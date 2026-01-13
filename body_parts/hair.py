from enum import Enum

from body_parts.base_body_parts import BaseBodyPart


class HairStyles(Enum):
    FUZZ = "fuzz"
    #implement other styles as needed

class Hair(BaseBodyPart):
    def __init__(self, style: HairStyles) -> None:
        super().__init__("Hair")
        self.style: HairStyles = style
        self.is_styled = False