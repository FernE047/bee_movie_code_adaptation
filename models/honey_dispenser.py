class HoneyDispenser:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.current_amount = capacity

    def dispense(self, amount: int) -> int:
        if amount > self.current_amount:
            dispensed = self.current_amount
            self.current_amount = 0
            return dispensed
        else:
            self.current_amount -= amount
            return amount