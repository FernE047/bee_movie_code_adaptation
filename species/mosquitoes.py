from species.base_specie import BaseSpecie


class Mosquito(BaseSpecie):
    def __init__(self) -> None:
        self.name = "Mosquito"
        self.can_fly_flag = True
        self.should_fly = True
