from species.base_specie import BaseSpecie


class Ladybug(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Ladybug")