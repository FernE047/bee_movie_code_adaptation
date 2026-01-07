from species.base_specie import BaseSpecie


class Mosquito(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Mosquito", can_fly=True, should_fly=True)