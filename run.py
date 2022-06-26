#intro
def intro():
    start_game = input("Do you wish to be a Hero? (Y/N)\n")
    if start_game.upper().strip() == "Y":
        pre_ascalon()
    elif start_game.upper().strip() == "N":
        print()
        print("Goodbye")

#ascalon
def pre_ascalon():
    print()
    f = open("prophecies/a-pre-ascalon/pre.text", "r")
    print(f.read())
    quest1 = input("Do you accept? (Y/N)\n")
    if quest1.upper().strip() == "N":
        print()
        print("The Charr eat you for breakfast")
        intro()
    elif quest1.upper().strip() == "Y":
        print()
        f = open("prophecies/a-pre-ascalon/pre-y", "r")
        print(f.read())
        post_ascalon()

def post_ascalon():
    print()
    print("You search around and find the King")
    quest2 = input("Do stay with the King? (Y/N)\n")
    if quest2.upper().strip() == "N":
        print()
        print("You leave with the prince")
        shiverpeaks()
    elif quest2.upper().strip() == "Y":
        print()
        print("You stay and retire \n")
        intro()

#title
print("         Guild Wars          ")
print(" Hello & welcome to Ascalon  ")
intro()