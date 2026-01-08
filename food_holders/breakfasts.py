from foods.base_food import BaseFood
from foods.honey import Honey


class Breakfast(BaseFood):
    def __init__(self) -> None:
        super().__init__(name="Breakfast", amount=1, unit="meal")
        self.ingredients: list[BaseFood] = []

    def prepare(self, honey: Honey) -> None:
        # Use honey to prepare breakfast items
        # it's assumed that breakfast requires both honey coffee and honey bread
        honey_coffee = honey.make_honey_coffee()
        honey_bread = honey.make_honey_bread()
        self.ingredients.append(honey_coffee)
        self.ingredients.append(honey_bread)

    def is_ready(self) -> bool:
        if len(self.ingredients) < 2:
            return False
        if not any(item.name == "Honey Coffee" for item in self.ingredients):
            return False
        if not any(item.name == "Honey Bread" for item in self.ingredients):
            return False
        return True

    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(ingredient) for ingredient in self.ingredients)}"
