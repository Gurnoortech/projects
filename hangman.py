import random
import os

list1 = []


# function for concatinating list
def concatination(list1):
    x = ""
    for i in range(len(list1)):
        x += list1[i]
    return x


# function for checking win
def check_win(choice, stringified):
    if choice == stringified:
        print("🎉YOU DID IT🎉\n🎉YOU WIN THE GAME🎉")
        exit()


os.system("cls")
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
choice = random.choice(rainbow)
length = choice.__len__()


print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
print("| Hint :- 🌈Rainbor colour🌈 |")
print("|____________________________|")
# loop for printing (_____) in starting.
for i in range(length):
    print("_", end=(""))
print()
# loop for printing concatinated main list.
for j in range(length):
    elements = "_"
    list1.append(elements)
# loop for taking input and replacing it with suitable index of (_____).
flag = 0
chances = 3 + length
for i in range(chances):
    # calling function to check win game option.
    check_win(choice, concatination(list1))
    # chances left for user to complete the game.
    print()
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("|❗you have", chances, "chance left ❗|")
    print("|___________________________|")
    # taking input of word.
    letter = input("enter the letter of your choice : ").lower()
    print()
    # loop for replacing input letter with empty space.
    os.system("cls")
    for j in range(length):
        if letter in choice:
            if letter == choice[flag] and list1[flag] == "_":
                list1[flag] = letter
                print(concatination(list1))
                break
        # if input letter dose'nt match with ramdom chossed word in game.
        else:
            print(concatination(list1))
            print("❌incorrect word❌")
            break
        flag += 1
    chances -= 1
    flag = 0
# if user lose all chances.
if chances == 0 and choice != concatination(list1):
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("|BETTER LUCK NEXT TIME|\n¦YOU LOSE THE GAME    ¦")
    print("|_____________________|")
else:
    print("🎉YOU DID IT🎉\n🎉YOU WIN THE GAME🎉")
