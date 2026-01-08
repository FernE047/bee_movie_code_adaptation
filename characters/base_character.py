from species.base_specie import BaseSpecie
from enum import Enum


class Emotion(Enum):
    NEUTRAL = "neutral"
    EXCITED = "excited"


class BaseCharacter:
    def __init__(self, name: str, nickname: str, species: BaseSpecie) -> None:
        self.name = name
        self.used_name_flag = False
        self.nickname = nickname
        self.species = species
        self.location: None | str = None
        self.emotion: Emotion = Emotion.NEUTRAL

    def build_action(self, action: str) -> str:
        return f"({action})"

    def action(self, action: str) -> None:
        print(self.build_action(action))

    def set_location(self, location: str) -> None:
        self.location = location
        self.action(f"{self.nickname} is now at {self.location}.")

    def set_emotion(self, emotion: Emotion) -> None:
        self.emotion = emotion

    def speak(self, text: str) -> None:
        if self.used_name_flag:
            print(f"{self.nickname}: {text}")
        else:
            print(f"{self.nickname} ({self.name}): {text}")
            self.used_name_flag = True
