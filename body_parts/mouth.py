from body_parts.base_body_parts import BaseBodyPart


class Mouth(BaseBodyPart):
    def __init__(self) -> None:
        super().__init__("Mouth")
        self.is_rinsed = False

    def speak(self, text: str) -> None:
        print(text)
