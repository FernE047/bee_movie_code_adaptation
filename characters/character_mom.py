from characters.base_character import BaseCharacter
from food_holders.breakfasts import Breakfast
from foods.honey import Honey
from species.bees import Bee


class Mom(BaseCharacter[Bee]):
    def __init__(self) -> None:
        super().__init__(name="Janet Benson", nickname="Mom", species=Bee())
        self.breakfast: None | Breakfast = None

    def get_honey_supply(self) -> Honey:
        return Honey(amount=200)

    def prepare_breakfast(self) -> None:
        honey = self.get_honey_supply()
        self.breakfast = Breakfast()
        self.breakfast.prepare(honey)
        if self.breakfast.is_ready():
            self.speak(
                f"{self.build_action('calling from downstairs')} Barry! Breakfast is ready!"
            )
        else:
            self.speak("Oh no, breakfast is not ready yet!")

    def serve_breakfast(self) -> Breakfast:
        if self.breakfast and self.breakfast.is_ready():
            return self.breakfast
        else:
            raise ValueError("Breakfast is not ready.")
