from species.base_specie import BaseSpecie
from enum import Enum


class Emotion(Enum):
    NEUTRAL = "neutral"
    EXCITED = "excited"


class BaseCharacter:
    def __init__(self, name: str, nickname: str, species: BaseSpecie) -> None:
        self.name = name
        self.nickname = nickname
        self.species = species
        self.location: None | str = None
        self.emotion: Emotion = Emotion.NEUTRAL

    def set_location(self, location: str) -> None:
        self.location = location
        print(f"{self.nickname} is now at {self.location}.")

    def set_emotion(self, emotion: Emotion) -> None:
        self.emotion = emotion

    def speak(self, text: str) -> None:
        print(f"{self.nickname}: {text}")