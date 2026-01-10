from characters.character_narrator import Narrator
from main_characters.character_barry import Barry
from food_holders.honey_dispenser import HoneyDispenser
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
    dispenser_at_bathroom = HoneyDispenser(capacity=100)
    barry.get_ready(dispenser_at_bathroom)
    mom = barry.get_mom()
    mom.set_location("Kitchen")
    mom.prepare_breakfast()
    barry.react_to_breakfast()


if __name__ == "__main__":
    main()
