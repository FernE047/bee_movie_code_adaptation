class BaseFood:
    def __init__(self, name: str, amount: int, unit: str) -> None:
        self.name = name
        self.amount = amount
        self.unit = unit

    def consume(self, quantity: int) -> None:
        if self.has_amount(quantity):
            self.amount -= quantity
        else:
            raise ValueError(
                f"Not enough {self.name} to consume the requested quantity."
            )

    def refill(self, quantity: int) -> None:
        self.amount += quantity

    def has_amount(self, quantity: int) -> bool:
        return self.amount >= quantity

    def __str__(self) -> str:
        return f"{self.amount} {self.unit} of {self.name}"
