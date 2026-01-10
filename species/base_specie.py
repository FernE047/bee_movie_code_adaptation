class BaseSpecie:
    def __init__(
        self, name: str, can_fly: bool = False, should_fly: bool = False
    ) -> None:
        self.name = name
        self.can_fly_flag = can_fly
        self.should_fly = should_fly

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
