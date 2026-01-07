# There's only one wardrobe in the bee movie universe, it's Barry's wardrobe

from models.clothes import Clothes


class Wardrobe:
    def __init__(self) -> None:
        self.clothes: list[Clothes] = []

    def fill_wardrobe(self) -> None:
        default_shirt = Clothes("Yellow, black")
        for _ in range(4):
            self.add_clothing(default_shirt)
        special_shirt = Clothes("black and yellow")
        self.add_clothing(special_shirt)

    def add_clothing(self, item: Clothes) -> None:
        self.clothes.append(item)
