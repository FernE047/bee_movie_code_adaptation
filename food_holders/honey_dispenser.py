from foods.honey import Honey


class HoneyDispenser:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.honey = Honey(amount=capacity)

    @property
    def current_level(self) -> int:
        return self.honey.amount

    def dispense(self, amount: int) -> Honey:
        if amount <= self.honey.amount:
            self.honey.consume(amount)
            return Honey(amount=amount)
        else:
            dispensed_amount = self.honey.amount
            self.honey.consume(dispensed_amount)
            return Honey(amount=dispensed_amount)