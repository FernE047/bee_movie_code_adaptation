from characters.base_character import BaseCharacter, Emotion
from models.honey_dispenser import HoneyDispenser
from models.wardrobe import Wardrobe
from species.bees import Bee


class Barry(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Barry Benson", nickname="Barry", species=Bee())
        self.set_emotion(Emotion.EXCITED)
        self.is_hair_styled = False
        self.is_mouth_rinsed = False
        self.is_armpits_honeyed = False
        self.honey_stored = 0

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

    def uses_honey(self, amount: int) -> None:
        if amount <= self.honey_stored:
            self.honey_stored -= amount
        else:
            self.action(
                f"{self.nickname} tries to use {amount} units of honey but only has {self.honey_stored}."
            )
            raise ValueError("Movie Over:Not enough honey stored.")

    def get_honey_from_dispenser(self, dispenser: HoneyDispenser, amount: int) -> None:
        dispensed = dispenser.dispense(amount)
        self.honey_stored += dispensed
        self.action(
            f"{self.nickname} gets {dispensed} units of honey from the dispenser."
        )

    def style_hair(self) -> None:
        self.is_hair_styled = True
        self.uses_honey(5)
        self.action(f"{self.nickname} uses honey to style his hair.")

    def rinse_mouth(self) -> None:
        self.is_mouth_rinsed = True
        self.uses_honey(3)
        self.action(f"{self.nickname} uses honey to rinse his mouth.")

    def honey_armpits(self) -> None:
        self.is_armpits_honeyed = True
        self.uses_honey(2)
        self.action(f"{self.nickname} then applies honey to his armpits.")

    def get_ready(self, dispenser: HoneyDispenser) -> None:
        self.get_honey_from_dispenser(dispenser, 10)
        self.style_hair()
        self.rinse_mouth()
        self.honey_armpits()
