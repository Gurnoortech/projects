def dice():
    import random

    dice = random.randrange(1, 7)
    match dice:
        case 1:
            for i in range(5):
                if i == 0:
                    print("¦‾‾‾‾‾‾‾‾‾‾‾¦")
                elif i == 4:
                    print("¦___________¦")
                elif i == 1 or i == 3:
                    print("¦           ¦")
                else:
                    print("¦     •     ¦")
        case 2:
            for i in range(5):
                if i == 0:
                    print("¦‾‾‾‾‾‾‾‾‾‾‾¦")
                elif i == 4:
                    print("¦___________¦")
                elif i == 1:
                    print("¦   •       ¦")
                elif i == 2:
                    print("¦           ¦")
                elif i == 3:
                    print("¦       •   ¦")
        case 3:
            for i in range(5):
                if i == 0:
                    print("¦‾‾‾‾‾‾‾‾‾‾‾¦")
                elif i == 4:
                    print("¦___________¦")
                elif i == 1:
                    print("¦   •       ¦")
                elif i == 2:
                    print("¦     •     ¦")
                elif i == 3:
                    print("¦       •   ¦")
        case 4:
            for i in range(5):
                if i == 0:
                    print("¦‾‾‾‾‾‾‾‾‾‾‾¦")
                elif i == 4:
                    print("¦___________¦")
                elif i == 2:
                    print("¦           ¦")
                else:
                    print("¦   •   •   ¦")
        case 5:
            for i in range(5):
                if i == 0:
                    print("¦‾‾‾‾‾‾‾‾‾‾‾¦")
                elif i == 4:
                    print("¦___________¦")
                elif i == 2:
                    print("¦     •     ¦")
                else:
                    print("¦   •   •   ¦")
        case 6:
            for i in range(5):
                if i == 0:
                    print("¦‾‾‾‾‾‾‾‾‾‾‾¦")
                elif i == 4:
                    print("¦___________¦")
                else:
                    print("¦   •   •   ¦")


# callig function.
import os

while True:
    os.system("cls")
    dice()
    input()
