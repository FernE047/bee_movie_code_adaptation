from characters.base_character import BaseCharacter
from food_holders.breakfasts import Breakfast
from foods.honey import Honey
from species.bees import Bee


class Mom(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Janet Benson", nickname="Mom", species=Bee())
        self.name="Janet Benson"
        self.nickname="Mom"
        self.species=Bee()

    def get_honey_supply(self) -> Honey:
        return Honey(amount=200)

    def prepare_breakfast(self) -> None:
        honey = self.get_honey_supply()
        breakfast = Breakfast()
        breakfast.prepare(honey)
        if breakfast.is_ready():
            self.speak(f"{self.build_action('calling from downstairs')} Barry! Breakfast is ready!")
        else:
            self.speak("Oh no, breakfast is not ready yet!")

