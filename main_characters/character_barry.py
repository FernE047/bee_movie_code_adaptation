from characters.base_character import BaseCharacter, Emotion
from characters.character_mom import Mom
from food_holders.breakfasts import Breakfast
from food_holders.honey_dispenser import HoneyDispenser
from foods.honey import Honey
from models.wardrobe import Wardrobe
from species.bees import Bee


class Barry(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Barry Benson", nickname="Barry", species=Bee())
        self.set_emotion(Emotion.EXCITED)
        self.is_hair_styled = False
        self.is_mouth_rinsed = False
        self.is_armpits_honeyed = False
        self.honey_stored = Honey(amount=0)
        self.mom: None | Mom = None

    def choose_clothing(self, wardrobe: Wardrobe) -> None:
        self.action(f"{self.nickname} is choosing clothes from his wardrobe.")
        for item in wardrobe.clothes:
            color = item.color
            if self.emotion == Emotion.EXCITED:
                if color == "Yellow, black":
                    self.speak(f"{color}.")
                elif color == "black and yellow":
                    self.speak(f"Ooh, {color}! Yeah, let's shake it up a little.")
                    break
            else:
                self.speak(
                    f"{color}. all right, I'll wear this one."
                )  # Simplified, because Barry is always excited
                break

    def get_honey_from_dispenser(self, dispenser: HoneyDispenser, amount: int) -> None:
        dispensed = dispenser.dispense(amount)
        self.honey_stored.refill(dispensed.amount)
        self.action(
            f"{self.nickname} gets {dispensed} units of honey from the dispenser."
        )

    def style_hair(self) -> None:
        self.is_hair_styled = True
        self.honey_stored.consume(5)
        self.action(f"{self.nickname} uses honey to style his hair.")

    def rinse_mouth(self) -> None:
        self.is_mouth_rinsed = True
        self.honey_stored.consume(3)
        self.action(f"{self.nickname} uses honey to rinse his mouth.")

    def honey_armpits(self) -> None:
        self.is_armpits_honeyed = True
        self.honey_stored.consume(2)
        self.action(f"{self.nickname} then applies honey to his armpits.")

    def get_ready(self, dispenser: HoneyDispenser) -> None:
        self.get_honey_from_dispenser(dispenser, 10)
        self.style_hair()
        self.rinse_mouth()
        self.honey_armpits()

    def get_mom(self) -> Mom:
        if self.mom is None:
            self.mom = Mom()
        return self.mom

    def react_to_breakfast_call(self, breakfast: Breakfast) -> None:
        if breakfast.is_ready():
            self.speak("Coming!")
        else:
            self.speak("What's for breakfast?")
