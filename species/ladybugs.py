from species.base_specie import BaseSpecie, WeightDescriptions


class Ladybug(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(
            name="Ladybug", weight=WeightDescriptions.LIGHT, has_wings=True
        )
