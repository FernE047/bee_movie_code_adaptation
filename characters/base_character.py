from species.base_specie import BaseSpecie


class BaseCharacter:
    def __init__(self, name: str, nickname: str, species: BaseSpecie) -> None:
        self.name = name
        self.nickname = nickname
        self.species = species

    def speak(self, line: str) -> None:
        print(f"{self.name}: {line}")
