from sys import exit
from random import randint
from textwrap import dedent
from time import sleep

import inventory
import health

class Scene(object):

    """An abstract base class"""

    def enter():
        print("Not yet implemented!")
        exit(1)

    def __print__(self, word):
        self.word = word
        sleep(2)
        print(self.word)

class Welcome(Scene):

    """Displays welcome info"""

    def enter(self):
        print("\n")
        print("-" * 33)
        print("Precarious! - A Game by Calvin Xu")
        print("-" * 33)

        sleep(2)

        return 'dungeon_ent'

class Death(Scene):

    why = [
        " because, alas, the chances were so against you.",
        ". You really should think before you act. Try again.",
        ". Don't be so rash!",
        ". You were sooo close...Try again."
    ]

    def enter(self):
        print("-" * 10)
        print("\n\nYou died{}".format(Death.why[randint(0, len(self.why)-1)]))
        print("-" * 10)
        exit(0)

class DungeonEntrance(Scene):

    def enter(self):
        sleep(1)
        print("\nYou are about to enter the ancient ruins.")
        sleep(1)
        reply = input("\nAre you prepared? Type [yes] or [no]: ")
        if reply == "yes":
            print("\nThen go in!")
            return 'hallway'
        else:
            return 'dungeon_ent'

class Hallway(Scene):

    def enter(self):
        super().__print__("\nYou enter a hallway. There are three gates.")
        super().__print__("\nWhich one do you want to enter?")
        sleep(2)
        response = input("\nType [left], [right], or [forward]: ")
        if response == "left":
            super().__print__("\nYou go through the gate to your left. Good luck!")
            return 'room1'

        elif response == "right":
            super().__print__("\nYou go through the gate to your right. Good luck!")
            return 'room2'

        elif response == "forward":
            super().__print__("\nYou go through the gate in front of you. Good luck!")
            return 'room3'

        else:
            return 'hallway'

class Room1(Scene):

    def enter(self):
        super().__print__("\nThe room is eeriely quiet.")
        super().__print__("\nSuddenly a dim, blue figure lights! It is a hologram.")
        super().__print__("\nThe hologram speaks:")
        super().__print__("\nI am Th...e..might..y...emperor...Jha...gz..emynnn [indistinguishable]...")
        super().__print__("\nTrespasser...")
        super().__print__("\nI charge...thee...")
        super().__print__("\nAnswer...thi...s...rid..dle...")
        super().__print__("\nOr flee...for thy life...")
        super().__print__("\nMark...")
        super().__print__("\n\"What..is..fast..er...than...war...rp..drive?..Rea..per, ranger, or..r, reporters fr..rom..Houuhg..Koumg [indistinguishable]?...\"")
        sleep(2)
        answer_riddle = input("\nType [reaper], [ranger], or [HK reporters]: ")


        if answer_riddle == "HK reporters":
            super().__print__("\nThe hologram nods, and gives you 1 HP. You recognize this as the ancient practice of +1s.")
            health.player.hpplus(1)
            health.player.hpcheck()
            inventory.backpack.potion()
            super().__print__("\nYou proceed to the next room.")

            return 'trap_hallway'

        else:
            super().__print__("\nThe emperor gets mad at you. He shouts:\"Naive!\";\"You are still too young!\";\"I'm angry.\" And suddenly you feel life taken away from you.")
            super().__print__("\nYou have a bad feeling about this.")
            health.player.hpminus(2)
            health.player.hpcheck()
            inventory.backpack.potion()
            super().__print__("\nYou proceed to the next room.")

            return 'trap_hallway'

class Room2(Scene):

    def enter(self):
        super().__print__("\nThe room shakes no sooner than you enter it!")
        super().__print__("\nA huge mechanical guardian rose shakily, shaking off millenia of dust. It looks like a crab with a turret on top.")
        super().__print__("\nIt has started locking on you with a laser beam! It's now or never! Defend yourself!")
        super().__print__("\nA rusty railgun to your right was just activated. You find with great relief that it can be manually controlled; bad news is it probably can only fire once.")
        super().__print__("\nThe mechanical chimera is slowly rising. It's legs looks fragile, but there a many of them. It's \"eye\" is worth a shot, but it is protected well with multiple lenses. It's neck was just exposed to you, but the armor is probably thick.")
        super().__print__("\nDecide where to fire at!")
        sleep(2)
        fire_answer = input("\nType [leg], [eye] or [neck]: ")

        if fire_answer == "neck":
            super().__print__("\nThe guardian's head falls clear off! The entire beast crumbles. Then there was silence. You defeated it!")
            super().__print__("\nYou even manage to scavenge a *droid service port*! Try use it on droids.")
            sleep(2)
            inventory.backpack.add_item("droid service port")
            super().__print__("\nYou proceed to the next room intact.")
            health.player.hpcheck()
            return 'room3'

        elif fire_answer == "eye":
            super().__print__("\nThe projectile pierces through many lenses but the eye is still largely intact.")
            super().__print__("\nThe guardian goes berserk at you and shot blue plasma. But its aim is affected so you are not too badly hurt. Then it exploded.")
            health.player.hpminus(1)
            health.player.hpcheck()
            super().__print__("\nYou even manage to scavenge a *droid service port*! Try use it on droids.")
            sleep(2)
            inventory.backpack.add_item("droid service port")
            super().__print__("\nYou are hurt but you proceed to the next room.")
            return 'room3'

        elif fire_answer == "leg":
            super().__print__("\nYou shoot off 2 legs, but 8 remain.")
            super().__print__("\nStill, the guardian temporarily loses balance and its shot does hit you squarely.")
            health.player.hpminus(2)
            health.player.hpcheck()
            super().__print__("\nYou are hurt, but you hide yourself and proceed to the next room while the beast recovers.")
            return 'room3'

        else:
            print("DOES NOT COMPUTE!")
            sleep(2)
            return 'room2'

class Room3(Scene):

    def enter(self):
        super().__print__("\nYou have entered an ancient edifice. It appears to be a library or database.")
        super().__print__("\nNow it has turned into a complete maze. Fortunately you have a map of it.")
        super().__print__(dedent("""
             Goal
               v
        ______  _____
        | 7|  _____ 4|
        |   1|_______|
        |  |_|  ___2 |
        |  |8 ____|  |
        |____|  _____|
              ^
            Start
        """))
        super().__print__("\nType the numbers on the beacons you encounter along the way to pass!")
        sleep(2)
        answer = input("\nBeacon sequence: ")

        if answer.isdigit():
            beacon = int(answer)
            if beacon == 281:
                super().__print__("\nYou walk out of the maze!")
                super().__print__("\nYou see dim light behind a wall. Investigate?")
                sleep(2)
                inves_answer = input("\nType [y] or [n]: ")
                if inves_answer == "y":
                    if randint(0, 1) < 1:
                        super().__print__("\nHey, you see a disabled droid. Maybe it holds important information.")
                        sleep(2)
                        hack_answer = input("\nTry hacking droid? Type [y] or [n]: ")
                        if hack_answer == "y":
                            if inventory.backpack.item_stat("droid service port"):
                                super().__print__("\n10001010101001010111001010101010101111101010" * 1000)
                                super().__print__('\nAccessing encrypted files...')
                                super().__print__('\nDecrypting....')
                                if randint(0,3) < 3:
                                    super().__print__("\n\n[SEN281 LOG-]")
                                    super().__print__("\n\n OVERRIDE CODE -- BUILTIN")
                                    super().__print__('\n\n-KRG - 4d7ve9o')
                                    super().__print__('\n\n SEN - rgt643i')
                                    super().__print__('\n\n-Impervious Grace - r58f7ti')
                                    super().__print__('\n\n-EliteCMD - tx39hdi')
                                    super().__print__('\n\n-TX9r99i..dkdf Drfds - ts++]?%')
                                    sleep(1)
                                    print("10001010101001010111001010101010101111101010" * 10)
                                    print("\n\n[System Report] Corrupt data. Further access failed.")
                                    inventory.inventory.backpack.add_item("code1")
                                    print("\nCool! This might come in handy.")
                                else:
                                    super().__print__("\nDecryption failed!")
                                    super().__print__("-" * 10)
                                    super().__print__("\nToo bad that happened.")
                            else:
                                super().__print__("\nYou do not have a *droid service port* to access droid memory bank.")
                        else:
                            super().__print__("\nOkay. It's probably safer not to mess around.")
                    else:
                        super().__print__("\nDodge! It's a sentry droid and it fired at you. You are hurt but fortunately it's set to stun.")
                        health.player.hpminus(1)
                        health.player.hpcheck()
                else:
                    super().__print__("\nOkay. It's probably safer not to mess around.")
            else:
                super().__print__("\nYou stumble inside the building, get lost and eventually starved to death.")
                return 'death'
        else:
            super().__print__("\nYou did not type a number and the system locked you in.")
            return 'death'

        inventory.backpack.potion()
        health.player.hpcheck()
        super().__print__("\nYou proceed to the next room.")
        return 'trap_hallway'

class TrapHallway(Scene):

    def enter(self):
        super().__print__("\nThis hallway is pitch dark.")
        super().__print__("\nYou unconsiously step backwards and step on a disconnected tripwire. Ancient technology haunts your path.")
        super().__print__("\nIt's a trap! You need to be able to see to get through.")
        sleep(2)

        if inventory.backpack.item_stat("night vision potion"):
            print("\nWhat do you do? Drink the suspicious *night vision potion*, or turn on the millenia old lighting system?")
            sleep(2)
            decision = input("\nType [drink potion] or [turn on lighting]: ")

            if decision == "drink potion":
                super().__print__("\nYou certainly feel nauseous...But you can see the hallway as in broad daylight.")
                super().__print__("\nOh! The agony! You are in pain, but you manage to get past all the hidden dangers and proceed to the next room.")
                inventory.backpack.remove_item("night vision potion")
                health.player.hpminus(1)
                health.player.hpcheck()
                return 'combat_room'
            elif decision == "turn on lighting":
                super().__print__("\nYou turn on the lighting. You look at the hideous traps for one split second before alarms go off!")
                super().__print__("\nThe defense mechanisms spring to life! You try to take cover, but there's none.")
                super().__print__("\nThree energy blasts shoot you squarely in the chest. Fortunately they are set to stun, and after millenia the wattage is low.")
                super().__print__("\nYou survive but is hurt badly. You proceed to the next room.")
                health.player.hpminus(3)
                health.player.hpcheck()
                return 'combat_room'
            else:
                print("DOES NOT COMPUTE!")
                sleep(2)
                return 'trap_hallway'
        else:
            print("\nI am afraid you have to turn on the millenia old lighting system.")
            decision = input("\nType [turn on lighting]: ")

            if decision == "turn on lighting":
                super().__print__("\nYou turn on the lighting. You look at the hideous traps for one split second before alarms go off!")
                super().__print__("\nThe defense mechanisms spring to life! You try to take cover, but there's none.")
                super().__print__("\nThree energy blasts shoot you squarely in the chest. Fortunately they are set to stun, and after millenia the wattage is low.")
                super().__print__("\nYou survive but is hurt badly. You proceed to the next room.")
                health.player.hpminus(3)
                health.player.hpcheck()
                return 'combat_room'
            else:
                print("DOES NOT COMPUTE!")
                sleep(2)
                return 'trap_hallway'


class CombatRoom(Scene):

    def enter(self):
        super().__print__("\nYou enter what seems to be a control room.")
        super().__print__("\nAn elite command droid is posted here! It sustains itself on energy pumped from fusion reactors below.")
        super().__print__("\nThis droid is very powerful.")
        super().__print__("\nDo you try sneak past it quietly, or duel with it?")
        sleep(2)
        combat_answer = input("\nType [sneak] or [duel]: ")

        if combat_answer == "sneak":
            if randint(0, 3) < 2:
                super().__print__("\nYou successfully sneak past it. What luck!")
                return 'boss'
            else:
                super().__print__("\nThe droid spots you! You hear the screeching sound of a target lock. A fusillade then followed.")
                health.player.hpminus(3)
                health.player.hpcheck()
                super().__print__("\nWhat a miracle! You survive and proceed to the next room.")
                return 'boss'

        elif combat_answer == "duel":
            super().__print__("\nYou hop onto the droid's neck and assault it with a monkey wrench.")
            if health.player.hp >= 3:
                super().__print__("\nIt's more effective than you previously think! You are strong enough that the droid cannot shake you off.")
                super().__print__("\nThe droid crumpled. Would you like to look at its memory banks?")
                sleep(2)
                hack_answer = input("\nType [y] or [n]: ")
                if hack_answer == "y":
                    if inventory.backpack.item_stat("droid service port"):
                        print("")
                        print("10001010101111001010001101111101010" * 1000)
                        super().__print__('\nAccessing encrypted files...')
                        super().__print__('\nDecrypting....')
                        if randint(0,3) < 3:
                            super().__print__("\n\n[CMD479 LOG-]\n")
                            super().__print__("-" * 42)
                            super().__print__("Impervious Grace Maintenance -- CLASSIFIED")
                            super().__print__('\n\n[ADMIN OVERRIDE]-Impervious Grace - r58f7ti')
                            super().__print__('\n\nMaintenance port located on plate 13, {the back}.')
                            super().__print__('\n\n-StsdaRd pr0ceDur53 - ts84hfbidn++]?%')
                            sleep(1)
                            print("")
                            print("1000101011110100101001010111001010101010101111101010" * 10)
                            super().__print__("\n\n[System Report] Corrupt data. Further access failed.")
                            inventory.backpack.add_item("code2")
                            print("Cool! This might come in handy.")
                        else:
                            super().__print__("\nDecryption failed!")
                            super().__print__("-" * 10)
                            super().__print__("\nToo bad that happened.")
                    else:
                        super().__print__("\nYou do not have a *droid service port* to access droid memory bank.")
                else:
                    super().__print__("\nOkay. It's probably safer not to mess around.")

            else:
                super().__print__("\nYou are too weak to do much serious damage. The droid shook you off and...")
                return 'death'

        else:
            super().__print__("DOES NOT COMPUTE!")
            return "combat_room"

        health.player.hpcheck()
        super().__print__("\nYou proceed to the next room.")
        return 'boss'

class Boss(Scene):

    def enter(self):
        super().__print__("\nYou look into the room and immediately realize that you have arrived at last.")
        super().__print__("\nAn obsidian tablet stands in the middle of the room, on a triangular pedestal.")
        super().__print__("\nYou slowly approach the sacred object, awe-struck.")
        super().__print__("\nYou reach out to it...")
        super().__print__("\nNo! A cracking sound boomed in the room. A guardian automaton rose. It is white, scorpion-like, dust-covered but emanating soft light.")
        super().__print__("\nIt looks hideous, and also invincible. It's totally covered in porcelain armour, and you cannot find even one weak point.")
        super().__print__("\nHaving no mood to marvel at ancient technology, you run to arm yourself.")
        super().__print__("\nYou find a railgun that shoots deadly projectiles, and a plasma cutter. Which one will stand against the beast?")
        super().__print__("\nWhich weapon will you use?")
        sleep(2)
        weapon = input("\nType [railgun], [plasma cutter], or [something else]: ")

        if weapon == "railgun":
            super().__print__("\nYou knock the automaton over with your railgun!")
            super().__print__("\nIt manages to fire a shot at you, but you are not too badly hurt.")
            health.player.hpminus(2)
            health.player.hpcheck()
            super().__print__("\nIt tries to get up, and in the commotion grab the obsidian tablet and ran away.")
            return 'win'

        elif weapon == "plasma cutter":
            super().__print__("\nYou cut its tail off. It loses it primary weapon!")
            super().__print__("\nBut it still manages to hit you with one of its mechanical legs. Fortunately the damage is relatively light.")
            health.player.hpminus(1)
            health.player.hpcheck()
            super().__print__("\nYou then swiftly maim the beast more and more. Eventually it crumbles. You grab the obsidian tablet and walk away.")
            return 'win'

        elif weapon == "something else":

            if inventory.backpack.item_stat("code1") or inventory.backpack.item_stat("code2") and inventory.backpack.item_stat("droid service port"):
                super().__print__("\nWhat do you do? Manual override? This suddenly occured to you.")
                sleep(2)
                answer = input("\nType [override]: ")

                if answer == "override":
                    super().__print__("\nYou swiftly circle the automaton, searching for the service port.")
                    super().__print__("\nThere it is! You plug in your console and try to hack.")
                    super().__print__("100101010001010101010111010101" * 1000)
                    print("\n\n")
                    super().__print__("-" * 40)
                    super().__print__("-Impervious Grace Maintenance Interface-")
                    super().__print__("\n[You are not the administrator of this system]")
                    super().__print__("\nCurrent automaton action: Neutralize all intruders.")
                    super().__print__("\nWith shakey fingers you type:")
                    super().__print__("\n[User]>sudo override\n")
                    sleep(1)
                    password = input("Admin override password: ")

                    if password == "r58f7ti":
                        super().__print__("\nAdmin action override...")
                        super().__print__("100101010001010101010111010101" * 1000)
                        sleep(2.56)
                        print("\n\nCommand complete in 2.56 sec")
                        print("-" * 10)
                        super().__print__("\nThe automaton settles down. You just casually grab the obsidian tablet and go away!")
                        health.player.hpcheck()
                        return 'win'
                    else:
                        print("\nIncorrect password. Access denied.")
                        super().__print__("\nThe automaton roars and sends you crashing into the floor.")
                        return 'death'
                else:
                    print("\nDOES NOT COMPUTE!")
                    return 'boss'
            else:
                print("\nYou really can't try anything else.")
                return 'boss'

        else:
            super().__print__("\nDOES NOT COMPUTE!")
            return "boss"

class Win(Scene):

    def enter(self):
        super().__print__("\nYou obatined the obsidian tablet, the sacred artifact from the deadly ruins! You won!")
        super().__print__("\nThank you for playing this game. Copyright Calvin Xu.")
        super().__print__("\n2017.7.24")
        super().__print__("\n(Certain events may be different on each playthrough.)")
        sleep(2)
        exit(0)
