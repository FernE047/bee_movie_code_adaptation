from characters.base_character import BaseCharacter, Emotion
from characters.character_mom import Mom
from food_holders.honey_dispenser import HoneyDispenser
from foods.honey import Honey
from models.wardrobe import Wardrobe
from species.bees import Bee


class Barry(BaseCharacter):
    def __init__(self) -> None:
        self.name = "Barry Benson"
        self.nickname = "Barry"
        self.species = Bee()
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
                self.speak(f"{color}. all right, I'll wear this one.")
                break

    def get_honey_from_dispenser(self, dispenser: HoneyDispenser, amount: int) -> None:
        dispensed = dispenser.dispense(amount)
        self.honey_stored.refill(dispensed.amount)
        self.action(f"{self.nickname} gets {dispensed} from the dispenser.")

    def uses_honey_action(self, honey_needed: int, success_message: str, failure_message: str, partial_message: str, set_flag: str) -> None:
        honey_used = self.honey_stored.consume(honey_needed)
        if honey_used == 0:
            setattr(self, set_flag, False)
            self.speak(failure_message)
        elif honey_used < honey_needed:
            setattr(self, set_flag, True)
            self.speak(partial_message)
        else:
            setattr(self, set_flag, True)
            self.action(success_message)

    def style_hair(self) -> None:
        self.uses_honey_action(
            honey_needed=5,
            success_message=f"{self.nickname} uses honey to style his hair.",
            failure_message="Uh oh, no honey left to style my hair! on my big day?!",
            partial_message="that should be enough honey to style my hair.",
            set_flag="is_hair_styled"
        )

    def rinse_mouth(self) -> None:
        self.uses_honey_action(
            honey_needed=3,
            success_message=f"{self.nickname} uses honey to rinse his mouth.",
            failure_message="We really need to buy more honey. My mouth is dry.",
            partial_message="just a little honey left, but I'll manage to rinse my mouth.",
            set_flag="is_mouth_rinsed"
        )

    def honey_armpits(self) -> None:
        self.uses_honey_action(
            honey_needed=2,
            success_message=f"{self.nickname} uses applies honey to his armpits.",
            failure_message="C'mon, we are bees and we don't have honey to honey our armpits? The horror!",
            partial_message="I'll have to make do with the little honey I have to honey my armpits.",
            set_flag="is_armpits_honeyed"
        )

    def get_ready(self, dispenser: HoneyDispenser) -> None:
        self.get_honey_from_dispenser(dispenser, 10)
        self.style_hair()
        self.rinse_mouth()
        self.honey_armpits()

    def get_mom(self) -> Mom:
        if self.mom is None:
            self.mom = Mom()
        return self.mom
    
    def react_to_breakfast(self) -> None:
        self.speak("Coming!")