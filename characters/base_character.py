from species.base_specie import BaseSpecie


class BaseCharacter:
    def __init__(self, name: str, nickname: str, species: BaseSpecie) -> None:
        self.name = name
        self.nickname = nickname
        self.species = species
        self.location: None|str = None

    def set_location(self, location: str) -> None:
        self.location = location
        print(f"{self.name} is now at {self.location}.")

    def speak(self, line: str) -> None:
        print(f"{self.name}: {line}")
