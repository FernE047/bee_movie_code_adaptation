from foods.base_food import BaseFood
from foods.honey_coffee import HoneyCoffee
from foods.honey_bread import HoneyBread

HONEY_COFFEE_HONEY_AMOUNT = 10
HONEY_BREAD_HONEY_AMOUNT = 20


class Honey(BaseFood):
    def __init__(self, amount: int) -> None:
        super().__init__(name="Honey", amount=amount, unit="ml")

    def drizzle(self, quantity: int) -> None:
        self.consume(quantity)

    def pour(self, quantity: int) -> None:
        self.consume(quantity)

    def make_honey_coffee(self) -> HoneyCoffee:
        self.consume(HONEY_COFFEE_HONEY_AMOUNT)
        return HoneyCoffee()

    def make_honey_bread(self) -> HoneyBread:
        self.consume(HONEY_BREAD_HONEY_AMOUNT)
        return HoneyBread()
