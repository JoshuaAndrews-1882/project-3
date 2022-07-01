import random
import os

os.system("")


class Style():
    """
    Text colors
    """
    YELLOW = '\u001b[33m'
    GREEN = '\u001b[32m'
    RED = '\u001b[31m'
    RESET = '\033[0m'


# intro
def intro():
    """
    This is the intro to game asking the user to enter their
    nname and if they want to play or not.
    Logo created using https://www.ascii-art-generator.org/
    """
    print(Style.YELLOW + """
  _____       _ _     _  __          __
 / ____|     (_) |   | | \ \        / /
| |  __ _   _ _| | __| |  \ \  /\  / /_ _ _ __ ___
| | |_ | | | | | |/ _` |   \ \/  \/ / _` | '__/ __|
| |__| | |_| | | | (_| |    \  /\  / (_| | |  \__ \.
 \_____|\__,_|_|_|\__,_|     \/  \/ \__,_|_|  |___/
\n """ + Style.RESET)
    print("            Hello & Welcome to Prophecies \n")
    global player_name
    while True:
        print()
        player_name = input("Enter your name: \n")
        print(f"Hi, {player_name} do you wish to be a Hero?")
        start_game = input("Please enter Y or N \n")
        os.system('clear')
        if start_game.upper().strip() == "Y":
            os.system('clear')
            pre_ascalon()
        elif start_game.upper().strip() == "N":
            print()
            os.system('clear')
            intro()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())
            print()


# PROPHECIES

# pre-ascalon
def pre_ascalon():
    """
    This is the first quest for the player with a simple
    yes or no question.
    If the wrong answer is chosen the game restarts.
    """
    while True:
        print()
        story = open("prophecies/pre-ascalon/pre.text", "r")
        print(story.read())
        quest1 = input("Do you accept? (Y/N)\n")
        os.system('clear')
        if quest1.upper().strip() == "N":
            print()
            story = open("prophecies/pre-ascalon/pre-n.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    pre_ascalon()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()

        elif quest1.upper().strip() == "Y":
            print()
            os.system('clear')
            story = open("prophecies/pre-ascalon/pre-y.text", "r")
            print(story.read())
            post_ascalon()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())
            print()


# post-ascalon
def post_ascalon():
    """
    This is the second quest with a yes or no question
    """
    while True:
        print()
        story = open("prophecies/post-ascalon/post.text", "r")
        print(story.read())
        quest2 = input("Do stay with the King? (Y/N)\n")
        os.system('clear')
        if quest2.upper().strip() == "N":
            print()
            os.system('clear')
            story = open("prophecies/post-ascalon/post-n.text", "r")
            print(story.read())
            shiverpeaks()
        elif quest2.upper().strip() == "Y":
            print()
            story = open("prophecies/post-ascalon/post-y.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    post_ascalon()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# shiverpeaks
def shiverpeaks():
    """
    This is the third quest with a simple yes or no question
    """
    while True:
        print()
        story = open("prophecies/shiverpeaks/shiver.text", "r")
        print(story.read())
        quest3 = input("Do you help the Deldrimor Dwarves (Y/N)\n")
        os.system('clear')
        if quest3.upper().strip() == "N":
            print()
            story = open("prophecies/shiverpeaks/shiver-n.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    shiverpeaks()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        elif quest3.upper().strip() == "Y":
            print()
            os.system('clear')
            story = open("prophecies/shiverpeaks/shiver-y.text", "r")
            print(story.read())
            kryta()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# kryta
def kryta():
    """
    This is the fourth quest with a simple yes or no question
    """
    while True:
        print()
        story = open("prophecies/kryta/kryta.text", "r")
        print(story.read())
        quest4 = input("Will you help fight the undead? (Y/N)\n")
        os.system('clear')
        if quest4.upper().strip() == "N":
            print()
            story = open("prophecies/kryta/kryta-n.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    kryta()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        elif quest4.upper().strip() == "Y":
            print()
            os.system('clear')
            story = open("prophecies/kryta/kryta-y.text", "r")
            print(story.read())
            dorian()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# dorian
def dorian():
    """
    This is the fifth quest, with a simple yes or no question
    """
    while True:
        print()
        story = open("prophecies/dorian/dorian.text", "r")
        print(story.read())
        quest5 = input("Do you choose to run away? (Y/N)\n")
        os.system('clear')
        if quest5.upper().strip() == "N":
            print()
            os.system('clear')
            story = open("prophecies/dorian/dorian-n.text", "r")
            print(story.read())
            chosen()
        elif quest5.upper().strip() == "Y":
            print()
            story = open("prophecies/dorian/dorian-y.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    dorian()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# chosen
def chosen():
    """
    This is the sixth quest, with a simple yes or no question
    """
    while True:
        print()
        story = open("prophecies/chosen/chosen.text", "r")
        print(story.read())
        quest6 = input("Will you stay and protect the Chosen? (Y/N)\n")
        os.system('clear')
        if quest6.upper().strip() == "N":
            print()
            os.system('clear')
            story = open("prophecies/chosen/chosen-n.text", "r")
            print(story.read())
            magumma()
        elif quest6.upper().strip() == "Y":
            print()
            story = open("prophecies/chosen/chosen-y.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    chosen()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# magumma
def magumma():
    """
    This is the seventh quest, with a yes or no question
    """
    while True:
        print()
        story = open("prophecies/magumma/magumma.text", "r")
        print(story.read())
        quest7 = input("Do you kill the Shining Blade? (Y/N)\n")
        os.system('clear')
        if quest7.upper().strip() == "N":
            print()
            os.system('clear')
            story = open("prophecies/magumma/magumma-n.text", "r")
            print(story.read())
            vizier()
        elif quest7.upper().strip() == "Y":
            print()
            story = open("prophecies/magumma/magumma-y.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    magumma()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# vizier
def vizier():
    """
    This is the eigth quest, with a simple yes or no question
    """
    while True:
        print()
        story = open("prophecies/vizier/vizier.text", "r")
        print(story.read())
        quest8 = input("Will you get the sceptor for Vizier? (Y/N)\n")
        os.system('clear')
        if quest8.upper().strip() == "N":
            print()
            story = open("prophecies/vizier/vizier-n.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    vizier()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        elif quest8.upper().strip() == "Y":
            print()
            os.system('clear')
            story = open("prophecies/vizier/vizier-y.text", "r")
            print(story.read())
            dunes()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# desert
def dunes():
    """
    This is the first quest that contains a game to pass.
    The game is rock, paper and scissors and they player
    must acheive 5 wins before the enemy to win.
    """

    player = 0
    enemy = 0

    print()
    story = open("prophecies/desert/dunes/dunes.text", "r")
    print(story.read())
    while True:
        print(Style.GREEN + f"{player_name}'s Score: " + Style.RESET, player)
        print(Style.RED + "Enemy Score: " + Style.RESET, enemy)
        quest9 = input("Pick your weapon! Rock, Paper or Scissors!: \n")
        game_choices = ["ROCK", "PAPER", "SCISSORS"]
        enemy_choice = random.choice(game_choices)
        if quest9.upper().strip() == enemy_choice:
            print(f"{player_name} and the enemy threw {quest9}. It's a draw!")
        elif quest9.upper().strip() == "ROCK":
            if enemy_choice == "SCISSORS":
                print(f"Rock smashes Scissors! {player_name} wins!")
                player += 1
            else:
                print(f"Paper covers Rock! {player_name} loses!")
                enemy += 1
        elif quest9.upper().strip() == "PAPER":
            if enemy_choice == "ROCK":
                print(f"Paper covers Pock! {player_name} wins!")
                player += 1
            else:
                print(f"Scissors cuts Paper! {player_name} loses!")
                enemy += 1
        elif quest9.upper().strip() == "SCISSORS":
            if enemy_choice == "PAPER":
                print(f"Scissors cuts Paper! {player_name} wins!")
                player += 1
            else:
                print(f"Rock smashes Scissors! {player_name} loses!")
                enemy += 1

        else:
            print()
            story = open("settings/rps.text", "r")
            print(story.read())

        if player == 5:
            print()
            os.system('clear')
            story = open("prophecies/desert/dunes/dunes-w.text", "r")
            print(story.read())
            elona()
        elif enemy == 5:
            print()
            story = open("prophecies/desert/dunes/dunes-l.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    dunes()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()


# elona
def elona():
    """
    This is the second quest with a game.
    It requires the player to guess the enemies number
    in 10 guesses or less to win.
    """
    enemy_number = random.randint(1, 200)
    attempt = 0

    print()
    story = open("prophecies/desert/elona/elona.text", "r")
    print(story.read())
    while True:
        try:
            print(Style.GREEN + "Attempts: " + Style.RESET, attempt)
            quest10 = int(input("Enter a number between 1 to 200: \n"))
            os.system('clear')
            if quest10 == enemy_number:
                print()
                os.system('clear')
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

        if attempt == 5:
            print()
            story = open("prophecies/desert/elona/elona-l.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    elona()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()


# thirsty
def thirsty():
    """
    This is the third quest with a game.
    It requires the player to guess heads or
    tails correctly 6 times to win.
    If they guess incorrectly 6 times first
    then they lose.
    """

    player = 0
    enemy = 0

    print()
    story = open("prophecies/desert/thirsty/thirsty.text", "r")
    print(story.read())
    while True:
        print(Style.GREEN + f"{player_name}'s Score: " + Style.RESET, player)
        print(Style.RED + "Enemy Score: " + Style.RESET, enemy)
        quest11 = input("Pick Heads or Tails! \n")
        os.system('clear')
        coin_choices = ["HEADS", "TAILS"]
        coin_flip = random.choice(coin_choices)
        if quest11.upper().strip() == coin_flip:
            print(f"{player_name} guessed correctly!")
            player += 1
        elif quest11.upper().strip() == "HEADS":
            if coin_flip == "TAILS":
                print(f"{player_name} didn't guess correctly!")
                enemy += 1
        elif quest11.upper().strip() == "TAILS":
            if coin_flip == "HEADS":
                print(f"{player_name} didn't guess correctly")
                enemy += 1

        else:
            print()
            story = open("settings/coin.text", "r")
            print(story.read())

        if player == 6:
            print()
            os.system('clear')
            story = open("prophecies/desert/thirsty/thirsty-w.text", "r")
            print(story.read())
            dragon()
        elif enemy == 6:
            print()
            story = open("prophecies/desert/thirsty/thirsty-l.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    thirsty()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()


# dragon
def dragon():
    """
    This is the fourt quest with a game to win.
    They player has to roll 3 dices and get higher
    than 10 to win.
    """
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
        if total >= 10:
            print()
            os.system('clear')
            print(Style.GREEN + "Total: " + Style.RESET, total)
            story = open("prophecies/desert/dragon/dragon-w.text", "r")
            print(story.read())
            southern()
        if total < 10:
            print()
            story = open("prophecies/desert/dragon/dragon-l.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    dragon()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()


# southern
def southern():
    """
    This quest is a simple yes or no question
    """
    while True:
        print()
        story = open("prophecies/southern/southern.text", "r")
        print(story.read())
        quest12 = input("Do you infuse your armor? (Y/N)\n")
        os.system('clear')
        if quest12.upper().strip() == "N":
            print()
            story = open("prophecies/southern/southern-n.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    southern()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        elif quest12.upper().strip() == "Y":
            print()
            os.system('clear')
            story = open("prophecies/southern/southern-y.text", "r")
            print(story.read())
            fire()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# fire
def fire():
    """
    This quest is a simple yes or no question
    """
    while True:
        print()
        story = open("prophecies/fire/fire.text", "r")
        print(story.read())
        quest13 = input("Do you open the Door of Komalie? (Y/N)\n")
        os.system('clear')
        if quest13.upper().strip() == "N":
            print()
            story = open("prophecies/fire/fire-n.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    fire()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()
        elif quest13.upper().strip() == "Y":
            print()
            os.system('clear')
            story = open("prophecies/fire/fire-y.text", "r")
            print(story.read())
            lich()
        else:
            print()
            story = open("settings/yesno.text", "r")
            print(story.read())


# lich
def lich():
    """
    This quest requires the player to win
    rock, paper and scissors 10 times before
    the enemy to win the game.
    """
    player = 0
    enemy = 0

    print()
    story = open("prophecies/lich/lich.text", "r")
    print(story.read())
    while True:
        print(Style.GREEN + f"{player_name}'s Score: " + Style.RESET, player)
        print(Style.RED + "Enemy Score: " + Style.RESET, enemy)
        quest13 = input("Pick your weapon! Rock, Paper or Scissors!: \n")
        game_choices = ["ROCK", "PAPER", "SCISSORS"]
        enemy_choice = random.choice(game_choices)
        if quest13.upper().strip() == enemy_choice:
            print(f"{player_name} and the Lich threw {quest13}! It's a draw!")
        elif quest13.upper().strip() == "ROCK":
            if enemy_choice == "SCISSORS":
                print(f"Rock smashes Scissors! {player_name} wins!")
                player += 1
            else:
                print(f"Paper covers Rock! {player_name} loses!")
                enemy += 1
        elif quest13.upper().strip() == "PAPER":
            if enemy_choice == "ROCK":
                print(f"Paper covers Rock! {player_name} wins!")
                player += 1
            else:
                print(f"Scissors cuts Paper! {player_name} loses!")
                enemy += 1
        elif quest13.upper().strip() == "SCISSORS":
            if enemy_choice == "PAPER":
                print(f"Scissors cuts Paper! {player_name} wins!")
                player += 1
            else:
                print(f"Rock smashes Scissors! {player_name} loses!")
                enemy += 1

        else:
            print()
            story = open("settings/rps.text", "r")
            print(story.read())

        if player == 10:
            print()
            os.system('clear')
            story = open("prophecies/lich/lich-w.text", "r")
            print(story.read())
            intro()
        elif enemy == 10:
            print()
            story = open("prophecies/lich/lich-l.text", "r")
            print(story.read())
            while True:
                play_again = input("Restart this quest? (Y/N) \n")
                if play_again.upper().strip() == "Y":
                    os.system('clear')
                    lich()
                elif play_again.upper().strip() == "N":
                    os.system('clear')
                    intro()
                else:
                    print()
                    story = open("settings/yesno.text", "r")
                    print(story.read())
                    print()


# title
intro()
