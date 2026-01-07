from characters.character_barry import Barry
from species.bees import Bee
from models.wardrobe import Wardrobe


def main() -> None:
    bee = Bee()
    bee.can_fly()
    barry = Barry()
    barry.set_location("Barry's House")
    wardrobe = Wardrobe()
    wardrobe.fill_wardrobe()

if __name__ == "__main__":
    main()