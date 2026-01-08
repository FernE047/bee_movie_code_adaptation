from foods.base_food import BaseFood


class HoneyCoffee(BaseFood):
    def __init__(self):
        super().__init__(name="Honey Coffee", amount=1, unit="cup")