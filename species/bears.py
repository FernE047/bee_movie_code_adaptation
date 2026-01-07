from species.base_specie import BaseSpecie


class Bear(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Bear")
