from body_parts.armpit import Armpit
from body_parts.base_body_parts import BaseBodyPart
from body_parts.hair import Hair
from body_parts.mouth import Mouth

class BaseSpecie:
    def __init__(
        self, name: str, can_fly: bool = False, should_fly: bool = False
    ) -> None:
        self.name = name
        self.can_fly_flag = can_fly
        self.should_fly = should_fly
        self.body_parts: list[BaseBodyPart] = []
        self.initialize_body_parts()

    def initialize_body_parts(self) -> None:
        self.mouth = Mouth()
        self.armpit = Armpit()
        self.hair = Hair()
        self.body_parts = [self.mouth, self.armpit, self.hair]

    def add_body_part(self, part: BaseBodyPart) -> None:
        self.body_parts.append(part)

    def get_name(self) -> str:
        return self.name

    def can_fly(self) -> str:
        if self.can_fly_flag:
            if self.should_fly:
                return f"{self.name}s can fly. they are so cool and aerodynamic!"
            else:
                return f"According to all known laws of aviation, there is no way that a {self.name} should be able to fly. Its wings are too small to get its fat little body off the ground. The {self.name}, of course, flies anyway because {self.name}s don't care what humans think is impossible."
        else:
            return f"{self.name}s cannot fly. they are grounded creatures. Boring!"

    def check_body_part(self, part_name: str) -> bool:
        for part in self.body_parts:
            if part.name.lower() == part_name.lower():
                return True
        return False
