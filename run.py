#intro
def intro():
    while True:
        print()
        start_game = input("Do you wish to be a Hero? (Y/N)\n")
        if start_game.upper().strip() == "Y":
            pre_ascalon()
        elif start_game.upper().strip() == "N":
            print()
            print("Goodbye")
        else:
            print()
            f = open("settings/yesno.text", "r")
            print(f.read())
            print()

#PROPHECIES

#ascalon
def pre_ascalon():
    while True:
        print()
        f = open("prophecies/pre-ascalon/pre.text", "r")
        print(f.read())
        quest1 = input("Do you accept? (Y/N)\n")
        if quest1.upper().strip() == "N":
            print()
            f = open("prophecies/pre-ascalon/pre-n.text", "r")
            print(f.read())
            intro()
        elif quest1.upper().strip() == "Y":
            print()
            f = open("prophecies/pre-ascalon/pre-y.text", "r")
            print(f.read())
            post_ascalon()
        else:
            print()
            f = open("settings/yesno.text", "r")
            print(f.read())
            print()

def post_ascalon():
    while True:
        print()
        f = open("prophecies/post-ascalon/post.text", "r")
        print(f.read())
        quest2 = input("Do stay with the King? (Y/N)\n")
        if quest2.upper().strip() == "N":
            print()
            f = open("prophecies/post-ascalon/post-n.text", "r")
            print(f.read())
            shiverpeaks()
        elif quest2.upper().strip() == "Y":
            print()
            f = open("prophecies/post-ascalon/post-y.text", "r")
            print(f.read())
            intro()
        else:
            print()
            f = open("settings/yesno.text", "r")
            print(f.read())

#shiverpeaks
def shiverpeaks():
    while True:
        print()
        f = open("prophecies/shiverpeaks/shiver.text", "r")
        print(f.read())
        quest3 = input("Do you help the Deldrimor Dwarves (Y/N)\n")
        if quest3.upper().strip() == "N":
            print()
            f = open("prophecies/shiverpeaks/shiver-n.text", "r")
            print(f.read())
            intro()
        elif quest3.upper().strip() == "Y":
            print()
            f = open("prophecies/shiverpeaks/shiver-y.text", "r")
            print(f.read())
            kryta()
        else:
            print()
            f = open("settings/yesno.text", "r")
            print(f.read())



#title
print("         Guild Wars          ")
print(" Hello & welcome to Ascalon  ")
intro()