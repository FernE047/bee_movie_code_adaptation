from species.base_specie import BaseSpecie


class Speaker(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Speaker")
