#simple calculator.
num1=float(input("enter the number : "))
num2=float(input("enter the number : "))
print("press 1 for addition. ")
print("press 2 for subtraction. ")
print("press 3 for multiplication. ")
print("press 4 for division. ")
num3=int(input("enter the number as per required result : "))
if num3==1:
    print(num1+num2)
elif num3==2:
    print(num1-num2)
elif num3==3:
    print(num1*num2)
elif num3==4:
    print(num1/num2)
else :
    print("invalid input")