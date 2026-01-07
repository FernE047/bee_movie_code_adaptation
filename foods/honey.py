from foods.base_food import BaseFood


class Honey(BaseFood):
    def __init__(self, amount: int) -> None:
        super().__init__(name="Honey", amount=amount, unit="ml")

    def drizzle(self, quantity: int) -> None:
        self.consume(quantity)
        
    def pour(self, quantity: int) -> None:
        self.consume(quantity)