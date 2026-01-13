from body_parts.wing import Wings
from species.base_specie import BaseSpecie, WeightDescriptions


class Ladybug(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(
            name="Ladybug", weight=WeightDescriptions.LIGHT, has_wings=True
        )
        self.wings = Wings()
        self.add_body_part(self.wings)
