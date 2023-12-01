#modified calculator.
num1=float(input("enter the number : "))
num2=float(input("enter the next number : "))
while True:
    choise=int(input("enter (1 for +)   (2 for -)   (3 for *)   (4 for /)   :"))
    if choise==1:
        num1=num1+num2
        print(num1)
    elif choise==2:
        num1=num1-num2
        print(num1)
    elif choise==3:
        num1=num1*num2
        print(num1)
    elif choise==4:
        num1=num1/num2
        print(num1)
    else :
        print("invalid input.")
    while True :
        x=input("want to continue ?    (yes or no)  : ".lower())
        if x=="yes" :
            num2=float(input("enter the next number : "))
            break
        elif x=="no" :
            print("thank you for calculation.")
            break
        else :
            print("invalid input.")
    if x=="no":
        break