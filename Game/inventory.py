from time import sleep

class Inventory(object):

    """A simple inventory system. Can add or remove multiple items at a time."""

    gear = []

    def show_gears(self):
        print(Inventory.gear)

    def add_item(self, *args):
        self.args = args
        for item in self.args:
            Inventory.gear.append(item)

    def remove_item(self, *args):
        self.args = args
        for item in self.args:
            Inventory.gear.remove(item)

    def item_stat(self, item):
        self.item = item

        if item in Inventory.gear:
            return True

        else:
            return False

    def potion(self):

        # A event that happens often

        sleep(2)
        print("\nHuh? There's a vial of *night vision potion* lying on the ground. Take it?")
        sleep(2)
        potion_answer = input("\nType y or n: ")

        if potion_answer == "y":
            backpack.add_item("night vision potion")
            sleep(2)
            print("\nYou got a *night vison potion*! Is it what it claims to be?")
        else:
            sleep(2)
            print("\nOkay. You leave the potion alone.")


backpack = Inventory()
