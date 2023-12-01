import os

os.system("cls")
# main list for storing data of ATM users as object.
obj_list = []


class ac_holder:
    def __init__(self, name, acno, pin, balance, log_st):
        self.name = name
        self.acno = int(acno)
        self.pin = int(pin)
        self.balance = int(balance)
        self.log_st = log_st

    # method for printing recipt of transcetion.
    def get_detail(self):
        print()
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(
            f"| name = {self.name}\n| account number = {self.acno}\n| balance = {self.balance}"
        )
        print("|___________________________")
        print()

    def save_log(self, statment):
        if len(self.log_st) > 4:
            del self.log_st[0]
        else:
            pass
        self.log_st.append(statment)

    def withdrawl(self, amount, pin):
        if amount <= self.balance and pin == self.pin:
            self.balance -= amount
            self.get_detail()
            var = f"debit amount = {amount} current balance = {self.balance}"
            self.save_log(var)
        else:
            print("invalid balance input or unmatch pin.")

    def deposite(self, amount, pin):
        if amount >= 0 and self.pin == pin:
            self.balance += amount
            self.get_detail()
            var = f"credit amount = {amount} current balance = {self.balance}"
            self.save_log(var)
        else:
            print("invalid balance input or unmatch pin.")

    def mini_statment(self, pin):
        if self.pin == pin:
            for i in self.log_st:
                print(i)
        else:
            print("unmatch pin.")

    def check_balance(self, pin):
        if self.pin == pin:
            self.get_detail()
        else:
            print("unmatch pin.")

    def pin_change(self):
        while True:
            flag = False
            try:
                new_pin = int(input("enter new pin :- "))
            except ValueError:
                print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                print(
                    "| invalid input.                 |\n| press any key to enter new pin |"
                )
                print("|________________________________|")
                input()
                os.system("cls")
                pass
            else:
                self.pin = new_pin
                flag = True
            if flag == True:
                break


# loader spliting text file's data
def load_obj(text):
    text_new = ""
    for i in text:
        if i == "\n":
            continue
        text_new += i
    objects = text_new.split("^")
    for object_ in objects:
        member = object_.split("~")
        trans_list = member[4][1:-1].split("$")
        if len(trans_list) > 0:
            obj_list.append(
                ac_holder(member[0], member[1], member[2], member[3], trans_list)
            )
        else:
            obj_list.append(ac_holder(member[0], member[1], member[2], member[3], []))

        # try:
        #     lst = y[4].split("$") '
        #     print(y[0], y[1], y[2], y[3], lst, "   after trans")
        #     # print(lst, "          trans list")
        #     obj_list.append(ac_holder(y[0], y[1], y[2], y[3], lst))
        # except:
        #     print(y[0], y[1], y[2], y[3], [], "    trans")
        #     obj_list.append(ac_holder(y[0], y[1], y[2], y[3], []))

        # obj_list.append(
        #         ac_holder(member[0], member[1], member[2], member[3], member[4])
        #     )
        # print(trans_list, "trans list")
        # print(member, "members")
        # print(member[0], member[1], member[2], member[3], member[4], "list")


file1 = open("atm.txt", "r")
string = f"{file1.read()}"


load_obj(string)
# print(obj_list, "(obj list)")
# print(obj_list[0].acno, obj_list[0].name, obj_list[0].pin)
# print(obj_list[1].acno, obj_list[1].name, obj_list[1].pin)
file1.close()


# update changes in text file.
# def update_data():
#     global obj_list
#     dummy_str = ""
#     for i in obj_list:
#         dummy_str += f"{i.name}~{i.acno}~{i.pin}~{i.balance}^"
#     return dummy_str[:-1]
def update_data():
    global obj_list
    dummy_str = ""
    dummy_2 = ""
    for i in obj_list:
        if len(i.log_st) > 0:
            for j in i.log_st:
                dummy_2 += f"{j}$"
        else:
            dummy_2 = " "
        dummy_str += f"{i.name}~{i.acno}~{i.pin}~{i.balance}~({dummy_2[:-1]})^"
        dummy_2 = ""

    # print(dummy_str[:-1])
    return dummy_str[:-1]


# first loop for whole process to run continously.
while True:
    # home page options.
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("| 1 for withdrawl.    |\n| 2 for deposit.      |\n| 3 for mini statment.|")
    print("| 4 for balance.      |\n| 5 for pin change.   |\n| 6 for exit.         |")
    print("|_____________________|")
    try:
        x = int(input(":- "))
        os.system("cls")
    except ValueError:
        x = 7
        os.system("cls")

    match x:
        # case 1 for withdrawl.
        case 1:
            # instruction for going back to home page.
            print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n|enter any key for main menu.|")
            print("|____________________________|")
            print()
            # inputs from ATM user as per requirement of transections.
            acc, amount, pin = (
                input("enter your account number :- "),
                input("enter your amount :- "),
                input("enter your pin :- "),
            )
            try:
                acc = int(acc)
                amount = int(amount)
                pin = int(pin)
            except ValueError:
                print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                print(
                    "| invalid input.              |\n| enter any key for main menu |"
                )
                print("|_____________________________|")
                input()
                os.system("cls")
                pass
            else:
                os.system("cls")
                for i in range(len(obj_list)):
                    # (if condition) search the user's account.
                    if acc == obj_list[i].acno:
                        # calling (withdrawl) method.
                        obj_list[i].withdrawl(amount, pin)
                        # updating balance in text file after transection.
                        file2 = open("atm.txt", "w")
                        file2.write(update_data())
                        file2.close()
                        input("press any key main menu :- ")
                        os.system("cls")
                        break
                else:
                    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                    print("| sorry             |\n| account not found |")
                    print("|___________________|")
                    print()
                    input("press any key for main menu :- ")
                    os.system("cls")
        # case 2 for deposit.
        case 2:
            # instruction for going back to home page.
            print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n|enter any key for main menu.|")
            print("|____________________________|")
            print()
            # inputs from ATM user as per requirement of transections.
            acc, amount, pin = (
                input("enter your account number :- "),
                input("enter your amount :- "),
                input("enter your pin :- "),
            )
            try:
                acc = int(acc)
                amount = int(amount)
                pin = int(pin)
            except ValueError:
                print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                print(
                    "| invalid input.              |\n| enter any key for main menu |"
                )
                print("|_____________________________|")
                input()
                os.system("cls")
                pass
            else:
                os.system("cls")
                for i in range(len(obj_list)):
                    # (if condition) search the user's account.
                    if acc == obj_list[i].acno:
                        # calling (deposite) method.
                        obj_list[i].deposite(amount, pin)
                        # updating balance in text file after transection.
                        file2 = open("atm.txt", "w")
                        file2.write(update_data())
                        file2.close()
                        input("press any key main menu :- ")
                        os.system("cls")
                        break
                else:
                    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                    print("| sorry             |\n| account not found |")
                    print("|___________________|")
                    print()
                    input("press any key for main menu :- ")
                    os.system("cls")
        # case 3 for mini statment.
        case 3:
            # instruction for going back to home page.
            print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n|enter any key for main menu.|")
            print("|____________________________|")
            print()
            # inputs to find the user's account.
            acc, pin = input("enter your account number :- "), input(
                "enter your pin :- "
            )
            try:
                acc = int(acc)
                pin = int(pin)
            except ValueError:
                print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                print(
                    "| invalid input.              |\n| enter any key for main menu |"
                )
                print("|_____________________________|")
                input()
                os.system("cls")
                pass
            else:
                os.system("cls")
                for i in range(len(obj_list)):
                    if obj_list[i].acno == acc:
                        obj_list[i].mini_statment(pin)
                        print()
                        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                        print("| enter any key for main menu |")
                        print("|_____________________________|")
                        input()
                        os.system("cls")
                        break
                else:
                    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                    print("| sorry             |\n| account not found |")
                    print("|___________________|")
                    print()
                    input("press any key for main menu :- ")
                    os.system("cls")
        # case 4 for cheaking balance.
        case 4:
            # instruction for going back to home page.
            print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n|enter any key for main menu.|")
            print("|____________________________|")
            print()
            # inputs from ATM user as per requirement of transections.
            acc, pin = (
                input("enter your account number :- "),
                input("enter your pin :- "),
            )
            try:
                acc = int(acc)
                pin = int(pin)
            except ValueError:
                print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                print(
                    "| invalid input.              |\n| enter any key for main menu |"
                )
                print("|_____________________________|")
                input()
                os.system("cls")
                pass
            else:
                os.system("cls")
                for i in range(len(obj_list)):
                    # (if condition) search the user's account.
                    if acc == obj_list[i].acno:
                        # calling (check_balance) method.
                        obj_list[i].check_balance(pin)
                        input("press any key main menu :- ")
                        os.system("cls")
                        break
                else:
                    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                    print("| sorry             |\n| account not found |")
                    print("|___________________|")
                    print()
                    input("press any key for main menu :- ")
                    os.system("cls")
        # case 5 for changing pin.
        case 5:
            # instruction for going back to home page.
            print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n|enter any key for main menu.|")
            print("|____________________________|")
            print()
            # inputs from ATM user as per requirement of transections.
            acc, pin = (
                input("enter your account number :- "),
                input("enter your pin :- "),
            )
            try:
                acc = int(acc)
                pin = int(pin)
            except ValueError:
                print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                print(
                    "| invalid input.              |\n| enter any key for main menu |"
                )
                print("|_____________________________|")
                input()
                os.system("cls")
                pass
            else:
                os.system("cls")
                for i in range(len(obj_list)):
                    # (if condition) search the user's account.
                    if acc == obj_list[i].acno and pin == obj_list[i].pin:
                        # calling (pin_change) method.
                        obj_list[i].pin_change()
                        # updating pin in text file after transection.
                        file2 = open("atm.txt", "w")
                        file2.write(update_data())
                        file2.close()
                        print("pin updated successfully.\npress any key main menu")
                        input(" :- ")
                        os.system("cls")
                        break
                else:
                    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                    print("| sorry             |\n| account not found |")
                    print("|___________________|")
                    print()
                    input("press any key for main menu :- ")
                    os.system("cls")
        case 6:
            exit()
        case 7:
            pass
