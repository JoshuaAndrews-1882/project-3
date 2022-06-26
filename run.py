# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def pre():
    f = open("story/pre-ascalon/pre.text", "r")
    print(f.read())
    quest1 = input("Do you accept? (Y/N)  ")
    if quest1 == "N":
        print("You die")
    elif quest1 == "Y":
        print("You help fight the Charr")
        post()

def post():
    print()
    print("You search around and find the King")
    quest2 = input("Do stay with the King? (Y/N)  ")
    if quest2 == "N":
        print("You leave with the prince")
        shiverpeaks()
    elif quest2 == "Y":
        print("You stay and retire")

print("         Guild Wars          ")
print(" Hello & welcome to Ascalon  ")
start_game = input("Do you wish to be a Hero? (Y/N)  ")

if start_game == "Y":
    pre()
elif start_game == "N":
    print("Goodbye")