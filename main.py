from characters.character_barry import Barry
from species.bees import Bee


def main() -> None:
    bee = Bee()
    bee.can_fly()
    barry = Barry()
    barry.set_location("Barry's House")

if __name__ == "__main__":
    main()