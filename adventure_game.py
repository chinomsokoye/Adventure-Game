import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def adventure_intro(item, evil_options):
    print_pause("\nYou find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + evil_options + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def field(item, evil_options):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        response1 = input("(Please enter 1 or 2.)\n")
        if response1 == "1":
            house_fight(item, evil_options)
            break
        elif response1 == "2":
            cave(item, evil_options)
            break


def house_fight(item, evil_options):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out "
                "steps a " + evil_options + ".")
    print_pause("Eep! This is the " + evil_options + "'s house!")
    print_pause("The " + evil_options + " attacks you!")
    if "Sword of Ogoroth" not in item:
        print_pause("You feel a bit under-prepared for this "
                    "what with only having a tiny dagger.")
    while True:
        response2 = input("Would you like to (1) fight or (2) run "
                          "away?")
        if response2 == "1":
            if "Sword of Ogoroth" in item:
                print_pause("As the " + evil_options + " moves to attack "
                            "you, you unsheath your new sword.")
                print_pause("The Sword of Orogoth shines brightly in "
                            "your hand as you brace yourself for the attack.")
                print_pause("But the " + evil_options + " takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("You have rid the town of the "
                            "" + evil_options + ". You are victorious!")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the "
                            "" + evil_options + ".")
                print_pause("You have been defeated!")
            play_again()
            break
        if response2 == "2":
            print_pause("You run back into the field. Luckily, "
                        "you don't seem to have been followed.")
            field(item, evil_options)
            break


def cave(item, evil_options):
    if "Sword of Ogoroth" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        print_pause("You walk back out to the field.")
        item.append("Sword of Ogoroth")
    field(item, evil_options)


def play_again():
    replay = input("Would you like to play again? (y/n)").lower()
    if replay == "y":
        print_pause("Excellent! Restarting the game...")
        play_game()
    elif replay == "n":
        print_pause("Thank's for playing! See you next time.")
    else:
        play_again()


def play_game():
    item = []
    evil_options = random.choice(["dragon", "troll", "gorgon",
                                 "wicked fairie", "pirate", "ghoul"])
    adventure_intro(item, evil_options)
    field(item, evil_options)


play_game()
