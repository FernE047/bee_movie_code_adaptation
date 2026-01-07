from species.base_specie import BaseSpecie


class Bee(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Bee", can_fly=True, should_fly=False)