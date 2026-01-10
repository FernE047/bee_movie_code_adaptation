from foods.base_food import BaseFood


class HoneyCoffee(BaseFood):
    def __init__(self) -> None:
        self.name = "Honey Coffee"
        self.amount = 1
        self.unit = "cup"
