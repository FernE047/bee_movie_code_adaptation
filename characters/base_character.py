from species.base_specie import BaseSpecie
from enum import Enum
from typing import TypeVar, Generic


class Emotion(Enum):
    NEUTRAL = "neutral"
    EXCITED = "excited"
    ANNOYED = "annoyed"


T = TypeVar('T', bound=BaseSpecie)


class BaseCharacter(Generic[T]):
    def __init__(self, name: str, nickname: str, species: T) -> None:
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

    def asks(self, question: str) -> None:
        self.speak(f"{question}?")

    def ask_known_name(self, other_character: "BaseCharacter[T]") -> None:
        self.asks(f"{other_character.nickname.title()}")
