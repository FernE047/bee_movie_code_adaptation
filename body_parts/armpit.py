from body_parts.base_body_parts import BaseBodyPart


class Armpit(BaseBodyPart):
    def __init__(self) -> None:
        super().__init__("Armpit")
        self.is_rinsed = False
