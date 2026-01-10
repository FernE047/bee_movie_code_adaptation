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

    def style_hair(self) -> None:
        honey_used = self.honey_stored.consume(5)
        if honey_used == 0:
            self.is_hair_styled = False
            self.speak("Uh oh, no honey left to style my hair! on my big day?!")
        elif honey_used < 5:
            self.is_hair_styled = True
            self.speak("that should be enough honey to style my hair.")
        else:
            self.is_hair_styled = True
            self.action(f"{self.nickname} uses honey to style his hair.")

    def rinse_mouth(self) -> None:
        honey_used = self.honey_stored.consume(3)
        if honey_used == 0:
            self.is_mouth_rinsed = False
            self.speak("We really need to buy more honey. My mouth is dry.")
        elif honey_used < 3:
            self.is_mouth_rinsed = True
            self.speak("just a little honey left, but I'll manage to rinse my mouth.")
        else:
            self.is_mouth_rinsed = True
            self.action(f"{self.nickname} uses honey to rinse his mouth.")

    def honey_armpits(self) -> None:
        honey_used = self.honey_stored.consume(2)
        if honey_used == 0:
            self.is_armpits_honeyed = False
            self.speak("C'mon, we are bees and we don't have honey to honey our armpits? The horror!")
        elif honey_used < 2:
            self.is_armpits_honeyed = True
            self.speak("I'll have to make do with the little honey I have to honey my armpits.")
        else:
            self.is_armpits_honeyed = True
            self.action(f"{self.nickname} uses applies honey to his armpits.")

    def get_ready(self, dispenser: HoneyDispenser) -> None:
        self.get_honey_from_dispenser(dispenser, 10)
        self.style_hair()
        self.rinse_mouth()
        self.honey_armpits()

    def get_mom(self) -> Mom:
        if self.mom is None:
            self.mom = Mom()
        return self.mom
