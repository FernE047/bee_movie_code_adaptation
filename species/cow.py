from species.base_specie import BaseSpecie


class Cow(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Cow")