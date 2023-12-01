import random
import os 
list1=['✊','✋','✌']
stone=1
paper=2
scissor=3
win=0
lose=0
tie=0
while True :
    os.system('cls')
    choise=int(input("enter (1 for ✊) (2 for ✋) (3 for ✌) : "))
    x=(random.choice(list1))
    if choise==1 :
        print("your choise : ✊")
    elif choise==2 :
        print("your choise : ✋")
    elif choise==3 :
        print("your choise : ✌")
    print("computer's choise :",x)
    if (choise==1 and x=="✊") or (choise==2 and x=="✋") or (choise==3 and x=="✌") :
        print(" ____________")
        print("|it was a tie|")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾")

        tie+=1
    elif (choise==1 and x=="✌") or (choise==2 and x=="✊") or (choise==3 and x=="✋"):
        print(" _______")
        print("|you win|")
        print(" ‾‾‾‾‾‾‾")
        win+=1
    elif (choise==1 and x=="✋") or (choise==2 and x=="✌") or (choise==3 and x=="✊") :
        print(" ________")
        print("|you lose|")
        print(" ‾‾‾‾‾‾‾‾")
        lose+=1
    else :
        print("invalid input.")
    while True :
        continution=input("Do you want to continue?        yes or no?  :".lower())
        if continution=="yes" :
            break
        elif continution=="no" :
            os.system('cls')
            print(f"Thankyou for playing.\nTotal attempts = {tie+lose+win}")
            print(f"Winnings = {win}\nLose = {lose}\nTie = {tie}")
            break
        else :
            print("invalid input.")
    if continution=="no" :
        break