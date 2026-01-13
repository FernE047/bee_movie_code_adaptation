from species.base_specie import BaseSpecie


class WaterBug(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Water bug", has_wings=True)
