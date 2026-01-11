from foods.base_food import BaseFood


class HoneyBread(BaseFood):
    def __init__(self) -> None:
        self.name = "Honey Bread"
        self.amount = 1
        self.unit = "loaf"
