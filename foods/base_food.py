class BaseFood:
    def __init__(self, name: str, amount: int, unit: str) -> None:
        self.name = name
        self.amount = amount
        self.unit = unit

    def consume(self, quantity: int) -> int:
        if self.has_amount(quantity):
            self.amount -= quantity
            return quantity
        else:
            consumed_amount = self.amount
            self.amount = 0
            return consumed_amount

    def refill(self, quantity: int) -> None:
        self.amount += quantity

    def has_amount(self, quantity: int) -> bool:
        return self.amount >= quantity

    def __str__(self) -> str:
        return f"{self.amount} {self.unit} of {self.name}"
