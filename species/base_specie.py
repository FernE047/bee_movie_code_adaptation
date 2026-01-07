class BaseSpecie:
    def __init__(self, name: str, can_fly: bool = False, should_fly: bool = False) -> None:
        self.name = name
        self.can_fly_flag = can_fly
        self.should_fly = should_fly

    def get_name(self) -> str:
        return self.name