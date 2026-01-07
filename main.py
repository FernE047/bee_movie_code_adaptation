from characters.character_narrator import Narrator
from characters.main_character_barry import Barry
from species.bees import Bee
from models.wardrobe import Wardrobe


def main() -> None:
    narrator = Narrator()
    bee = Bee()
    narrator.speak(bee.can_fly())
    barry = Barry()
    barry.set_location("Barry's Room")
    wardrobe = Wardrobe()
    wardrobe.fill_wardrobe()
    barry.choose_clothing(wardrobe)


if __name__ == "__main__":
    main()
