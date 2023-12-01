#Guess the number game.
import random
count=0
trail=8
x=(random.randrange(1,100))
while x>0:
    count+=1
    trail-=1
    num=int(input("Guess the number between 1 to 100 : "))
    if num==x:
        print("Congratulations.")
        print("You did it.")
        break
    if count==8:
        print("You lose the game.")
        print("Number of trails are over.")
        break
    elif num>x:
        print("Guessed number is to large.")
        print(trail,"trails left.")
    elif num<x:
        print("Guessed number is to small.")
        print(trail,"trails left.")
    else :
        print("Invalid input.")
print("Your total number of trails are = ",count)








