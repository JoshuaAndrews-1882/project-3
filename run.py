import random
"""
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
        quest8 = input("Will you get the sceptor for Vizier? (Y/N)\n")
        if quest8.upper().strip() == "N":
            print()
            story = open("prophecies/vizier/vizier-n.text", "r")
            print(story.read())
            intro()
        elif quest8.upper().strip() == "Y":
            print()
            story = open("prophecies/vizier/vizier-y.text", "r")
            print(story.read())
            dunes()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())

# desert
def dunes():

    player = 0
    enemy = 0

    print()
    story = open("prophecies/desert/dunes/dunes.text", "r")
    print(story.read())
    while True:
        print("Player Score: ", player)
        print("Enemy Score: ", enemy)
        quest9 = input("Pick your weapon! Rock, Paper or Scissors!: \n")
        game_choices = ["ROCK", "PAPER", "SCISSORS"]
        enemy_choice = random.choice(game_choices)
        if quest9.upper().strip() == enemy_choice:
            print(f"You and the enemy threw {quest9}. Keep fighting!")
        elif quest9.upper().strip() == "ROCK":
            if enemy_choice == "SCISSORS":
                print("Rock smashes scissors! You win!")
                player += 1
            else:
                print("Paper covers rock! You lose.")
                enemy += 1
        elif quest9.upper().strip() == "PAPER":
            if enemy_choice == "ROCK":
                print("Paper covers rock! You win!")
                player += 1
            else:
                print("Scissors cuts paper! You lose.")
                enemy += 1
        elif quest9.upper().strip() == "SCISSORS":
            if enemy_choice == "PAPER":
                print("Scissors cuts paper! You win!")
                player += 1
            else:
                print("Rock smashes scissors! You lose.")
                enemy += 1

        else:
            print()
            story = open("settings/rps.text", "r")
            print(story.read())

        if player == 5:
            print()
            story = open("prophecies/desert/dunes/dunes-w.text", "r")
            print(story.read())
            elona()
        elif enemy == 5:
            print()
            story = open("prophecies/desert/dunes/dunes-l.text", "r")
            print(story.read())
            intro()

# elona 
def elona():

    enemy_number = random.randint(1, 200)
    attempt = 0
    
    print()
    story = open("prophecies/desert/elona/elona.text", "r")
    print(story.read())
    while True:
        try:
            print("Attempts: ", attempt)
            quest10 = int(input("Enter a number between 1 to 200: \n"))
            if quest10 == enemy_number:
                print()
                story = open("prophecies/desert/elona/elona-w.text", "r")
                print(story.read())
                thirsty()
            elif quest10 < enemy_number:
                print()
                print("Too low")
                attempt += 1
            elif quest10 > enemy_number:
                print()
                print("Too high")
                attempt += 1
        except ValueError:
            print()
            story = open("settings/number.text", "r")
            print(story.read())

        if attempt == 10:
            print()
            story = open("prophecies/desert/elona/elona-l.text", "r")
            print(story.read())
            intro()

# thirsty
def thirsty():

    player = 0
    enemy = 0

    print()
    story = open("prophecies/desert/thirsty/thirsty.text", "r")
    print(story.read())
    while True:
        print("Player Score: ", player)
        print("Enemy Score: ", enemy)
        quest11 = input("Pick Heads or Tails! \n")
        coin_choices = ["HEADS", "TAILS"]
        coin_flip = random.choice(coin_choices)
        if quest11.upper().strip() == coin_flip:
            print("You guess the correct side of the coin!")
            player += 1
        elif quest11.upper().strip() == "HEADS":
            if coin_flip == "TAILS":
                print("You didn't guess the correct side of the coin!")
                enemy += 1
        elif quest11.upper().strip() == "TAILS":
            if coin_flip == "HEADS":
                print("You didn't guess the correct side of the coin!")
                enemy += 1
        
        else:
            print()
            story = open("settings/coin.text", "r")
            print(story.read())
        
        if player == 6:
            print()
            story = open("prophecies/desert/thirsty/thirsty-w.text", "r")
            print(story.read())
            dragon()
        elif enemy == 6:
            print()
            story = open("prophecies/desert/thirsty/thirsty-l.text", "r")
            print(story.read())
            intro()

# dragon
def dragon():

    total = 0

    print()
    story = open("prophecies/desert/dragon/dragon.text", "r")
    print(story.read())
    while True:
        print()
        input("Press any key when you wish to roll the dice \n")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        dice = [dice1, dice2, dice3]
        total_dice = sum(dice)
        total += total_dice
        print("Total: ", total)
        if total >= 10:
            print()
            story = open("prophecies/desert/dragon/dragon-w.text", "r")
            print(story.read())
            southern()
        if total < 10:
            print()
            story = open("prophecies/desert/dragon/dragon-l.text", "r")
            print(story.read())
            intro()
"""
# southern
def southern():
    while True:
        print()
        story = open("prophecies/southern/southern.text", "r")
        print(story.read())
        quest12 = input("Do you infuse your armor? (Y/N)\n")
        if quest12.upper().strip() == "N":
            print()
            story = open("prophecies/southern/southern-n.text", "r")
            print(story.read())
            intro()
        elif quest12.upper().strip() == "Y":
            print()
            story = open("prophecies/southern/southern-y.text", "r")
            print(story.read())
            fire()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


 
# title
print("         Guild Wars          ")
print(" Hello & welcome to Ascalon  ")
southern()