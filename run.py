# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def pre():
    print()
    f = open("story/pre-ascalon/pre.text", "r")
    print(f.read())
    quest1 = input("Do you accept? (Y/N)\n")
    if quest1 == "N":
        print()
        print("You die")
    elif quest1 == "Y":
        print()
        f = open("story/pre-ascalon/pre-y", "r")
        print(f.read())
        post()

def post():
    print()
    print("You search around and find the King")
    quest2 = input("Do stay with the King? (Y/N)\n")
    if quest2 == "N":
        print()
        print("You leave with the prince")
        shiverpeaks()
    elif quest2 == "Y":
        print()
        print("You stay and retire")

print("         Guild Wars          ")
print(" Hello & welcome to Ascalon  ")
start_game = input("Do you wish to be a Hero? (Y/N)\n")

if start_game == "Y":
    pre()
elif start_game == "N":
    print()
    print("Goodbye")