from characters.base_character import BaseCharacter, Emotion
from models.wardrobe import Wardrobe
from species.bees import Bee


class Barry(BaseCharacter):
    def __init__(self) -> None:
        super().__init__(name="Barry Benson", nickname="Barry", species=Bee())
        self.set_emotion(Emotion.EXCITED)

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
