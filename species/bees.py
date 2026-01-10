from species.base_specie import BaseSpecie


class Bee(BaseSpecie):
    def __init__(self) -> None:
        self.name = "Bee"
        self.can_fly_flag = True
        self.should_fly = False
