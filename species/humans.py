from species.base_specie import BaseSpecie


class Human(BaseSpecie):
    def __init__(self) -> None:
        super().__init__(name="Human")
