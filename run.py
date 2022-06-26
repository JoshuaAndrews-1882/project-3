# intro
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
            story = open("settings/yesno.text", "r")
            print(story.read())
            print()

# PROPHECIES

# ascalon
def pre_ascalon():
    while True:
        print()
        story = open("prophecies/pre-ascalon/pre.text", "r")
        print(story.read())
        quest1 = input("Do you accept? (Y/N)\n")
        if quest1.upper().strip() == "N":
            print()
            story = open("prophecies/pre-ascalon/pre-n.text", "r")
            print(story.read())
            intro()
        elif quest1.upper().strip() == "Y":
            print()
            story = open("prophecies/pre-ascalon/pre-y.text", "r")
            print(story.read())
            post_ascalon()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())
            print()

def post_ascalon():
    while True:
        print()
        story = open("prophecies/post-ascalon/post.text", "r")
        print(story.read())
        quest2 = input("Do stay with the King? (Y/N)\n")
        if quest2.upper().strip() == "N":
            print()
            story = open("prophecies/post-ascalon/post-n.text", "r")
            print(story.read())
            shiverpeaks()
        elif quest2.upper().strip() == "Y":
            print()
            story = open("prophecies/post-ascalon/post-y.text", "r")
            print(story.read())
            intro()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())

# shiverpeaks
def shiverpeaks():
    while True:
        print()
        story = open("prophecies/shiverpeaks/shiver.text", "r")
        print(story.read())
        quest3 = input("Do you help the Deldrimor Dwarves (Y/N)\n")
        if quest3.upper().strip() == "N":
            print()
            story = open("prophecies/shiverpeaks/shiver-n.text", "r")
            print(story.read())
            intro()
        elif quest3.upper().strip() == "Y":
            print()
            story = open("prophecies/shiverpeaks/shiver-y.text", "r")
            print(story.read())
            kryta()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())

# kryta
def kryta():
    while True:
        print()
        story = open("prophecies/kryta/kryta.text", "r")
        print(story.read())
        quest4 = input("Will you help fight the undead? (Y/N)\n")
        if quest4.upper().strip() == "N":
            print()
            story = open("prophecies/kryta/kryta-n.text", "r")
            print(story.read())
            intro()
        elif quest4.upper().strip() == "Y":
            print()
            story = open("prophecies/kryta/kryta-y.text", "r")
            print(story.read())
            dorian()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())

# dorian
def dorian():
    while True:
        print()
        story = open("prophecies/dorian/dorian.text", "r")
        print(story.read())
        quest5 = input("Do you choose to run away? (Y/N)\n")
        if quest5.upper().strip() == "N":
            print()
            story = open("prophecies/dorian/dorian-n.text", "r")
            print(story.read())
            chosen()
        elif quest5.upper().strip() == "Y":
            print()
            story = open("prophecies/dorian/dorian-y.text", "r")
            print(story.read())
            intro()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())

# chosen
def chosen():
    while True:
        print()
        story = open("prophecies/chosen/chosen.text", "r")
        print(story.read())
        quest6 = input("Will you stay and protect the Chosen? (Y/N)\n")
        if quest6.upper().strip() == "N":
            print()
            story = open("prophecies/chosen/chosen-n.text", "r")
            print(story.read())
            magumma()
        elif quest6.upper().strip() == "Y":
            print()
            story = open("prophecies/chosen/chosen-y.text", "r")
            print(story.read())
            intro()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())

# magumma
def magumma():
    while True:
        print()
        story = open("prophecies/magumma/magumma.text", "r")
        print(story.read())
        quest7 = input("Do you kill the Shining Blade? (Y/N)\n")
        if quest7.upper().strip() == "N":
            print()
            story = open("prophecies/magumma/magumma-n.text", "r")
            print(story.read())
            vizier()
        elif quest7.upper().strip() == "Y":
            print()
            story = open("prophecies/magumma/magumma-y.text", "r")
            print(story.read())
            intro()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())

# vizier
def vizier():
    while True:
        print()
        story = open("prophecies/vizier/vizier.text", "r")
        print(story.read())
        quest7 = input("Will you get the sceptor for Vizier? (Y/N)\n")
        if quest7.upper().strip() == "N":
            print()
            story = open("prophecies/vizier/vizier-n.text", "r")
            print(story.read())
            intro()
        elif quest7.upper().strip() == "Y":
            print()
            story = open("prophecies/vizier/vizier-y.text", "r")
            print(story.read())
            desert()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())

# title
print("         Guild Wars          ")
print(" Hello & welcome to Ascalon  ")
intro()