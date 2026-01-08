from foods.base_food import BaseFood


class HoneyBread(BaseFood):
    def __init__(self) -> None:
        super().__init__(name="Honey Bread", amount=1, unit="loaf")