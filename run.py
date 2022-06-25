# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def pre():
    print()
    print("King Adelbern calls for all heroes to help fight Charr")
    quest1 = input("do you join him? Y/N")
    if quest1 == "N":
        print("You die")
    elif quest1 == "Y":
        post()


print("         Guild Wars          ")
print(" Hello & welcome to Ascalon  ")
start_game = input("Do you wish to be a Hero? (Y/N)")

if start_game == "Y":
    pre()
elif start_game == "N":
    print("Goodbye")