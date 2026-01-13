from characters.base_character import BaseCharacter, Emotion
from species.bees import Bee


class Antenna:
    def __init__(self, ringtone: str) -> None:
        self.ringtone: str = ringtone
        self.is_ringing = False
        self.owner: None | BaseCharacter[Bee] = None
        self.caller: None | BaseCharacter[Bee] = None

    def set_owner(self, owner: BaseCharacter[Bee]) -> None:
        self.owner = owner

    def rings(self, caller: BaseCharacter[Bee]) -> None:
        if self.owner is None:
            return
        self.is_ringing = True
        self.caller = caller
        self.owner.action("phone ringing")
        for _ in range(3):
            self.owner.action(f"{self.ringtone}... {self.ringtone}...")
        self.owner.set_emotion(Emotion.ANNOYED)
        self.owner.speak("oh, hang on a second.")

    def answers(self) -> None:
        if self.owner is None or not self.is_ringing or self.caller is None:
            return
        self.owner.action("adjusts his antennas into a headset")
        self.is_ringing = False
        self.owner.set_emotion(Emotion.ANNOYED)
        self.owner.asks("Hello")

    def hangs_up(self) -> None:
        if self.owner is None:
            return
        self.owner.action("hangs up")
        self.is_ringing = False
        self.caller = None
