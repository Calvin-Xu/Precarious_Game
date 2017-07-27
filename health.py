from sys import exit
from time import sleep

class Health(object):

    """A simple player HP system"""

    hp = 6

    def hpcheck(self):
        sleep(2)
        print("")
        print("-" * 10)
        print(f"Your current health point is: {Health.hp}.")
        print("-" * 10)

        if Health.hp <= 0:
            print("\nYou have suffered too much to be saved.")
            print("Play again!")
            exit(0)

        else:
            pass

    def hpplus(self, val):
        Health.hp += val
        sleep(2)
        print(f"\nYou gained {val} hp!")

    def hpminus(self, val):
        Health.hp -= val
        sleep(2)
        print(f"\nYou lost {val} hp!")

player = Health()
