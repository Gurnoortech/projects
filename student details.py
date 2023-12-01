import os

# class making object students in memory.
main_list = []


class student:
    def __init__(self, Class, name, rollnumber):
        self.Class = int(Class)
        self.name = name
        self.rollnumber = int(rollnumber)


def load_obj(text):
    x = text.split("^")
    for i in x:
        y = i.split("~")
        main_list.append(student(y[0], y[1], y[2]))


file1 = open("test.txt", "r")
string = f"{file1.read()}"


load_obj(string)
file1.close()


def update_data():
    global main_list
    dummy_str = ""
    for i in main_list:
        dummy_str += f"{i.Class}~{i.name}~{i.rollnumber}^"
    return dummy_str[:-1]


while True:
    print(
        "press 1 for adding new student.\n      2 for viewing.\n      3 for deleting.\n      4 for updating."
    )
    x = int(input(":- "))
    os.system("cls")
    match x:
        # case 1 adding new student.
        case 1:
            while True:
                print("enter * to go back.")
                print("Adding new student in which class ? ")
                print("class 1\nclass 2\nclass 3\nclass 4\nclass 5")
                # class in which new student is getting added.
                class_num = input("enter class number :- ")
                os.system("cls")
                # count = number of new enteries user want to input in the data details.
                if class_num == "*":
                    break
                else:
                    print("enter * to go back.")
                    count = input("number of enteries :- ")
                    if count == "*":
                        os.system("cls")
                        break
                    else:
                        for i in range(int(count)):
                            name, rollnumber = (input(f"name :- ")), int(
                                input(f"   rollnumber :- ")
                            )
                            file2 = open("test.txt", "w")
                            main_list.append(student(class_num, name, rollnumber))
                            file2.write(update_data())
                            file2.close()
        # case 2 viewing student details.
        case 2:
            while True:
                print("enter * to go back.")
                print(
                    "press 1 for viewing all students in a perticular class.\n      2 for viewing a perticular students."
                )
                view = input(":- ")
                os.system("cls")
                match view:
                    # case 1 viewing all students in a class.
                    case "1":
                        class_number = int(input("enter class number :- "))
                        flag = False
                        for i in range(len(main_list)):
                            if class_number == main_list[i].Class:
                                print(
                                    f"Name = {main_list[i].name}\nRollnumber = {main_list[i].rollnumber}"
                                )
                                flag = True
                        if flag == False:
                            print("not found")
                    # case 2 viwing a particular student.
                    case "2":
                        class_number, roll = int(input("enter class number :- ")), int(
                            input("rollnumber :- ")
                        )
                        os.system("cls")
                        flag = False
                        for i in range(len(main_list)):
                            if (
                                class_number == main_list[i].Class
                                and roll == main_list[i].rollnumber
                            ):
                                print(
                                    f"Class = {main_list[i].Class}\nName = {main_list[i].name}\nRollnumber = {main_list[i].rollnumber}"
                                )
                                flag = True
                        if flag == False:
                            print("not found")
                    # case * to go back
                    case "*":
                        break
                    # case _ if user entered invalid input.
                    case _:
                        print("invalid input.")
        # case 3 deleting a details of student.
        case 3:
            while True:
                print("enter * to go back.")
                class_numb = input("enter class number :- ")
                if class_numb == "*":
                    os.system("cls")
                    break
                else:
                    class_number = int(class_numb)
                    roll = int(input("rollnumber :- "))
                    # print(class_number,"iurycgf")
                    flag = False
                    for i in range(len(main_list)):
                        os.system("cls")
                        if (
                            class_number == main_list[i].Class
                            and roll == main_list[i].rollnumber
                        ):
                            del main_list[i]
                            file3 = open("test.txt", "w")
                            file3.write(update_data())
                            file3.close()
                            flag = True
                            break
                    if flag == False:
                        print("not found")
        # case 4 updating details of student.
        case 4:
            while True:
                print("enter * to go back.")
                class_numb = input("enter class number :- ")
                if class_numb == "*":
                    os.system("cls")
                    break
                else:
                    class_number, roll = int(class_numb), int(input("rollnumber :- "))
                    flag = False
                    for i in range(len(main_list)):
                        if (
                            class_number == main_list[i].Class
                            and roll == main_list[i].rollnumber
                        ):
                            print(
                                f"Class = {main_list[i].Class}\nName = {main_list[i].name}\nRollnumber = {main_list[i].rollnumber}"
                            )
                            main_list[i].Class = int(input("updated class number :- "))
                            main_list[i].name = input("updated name :- ")
                            main_list[i].rollnumber = int(
                                input("updated rollnumber :- ")
                            )
                            print(
                                f"Class = {main_list[i].Class}\nName = {main_list[i].name}\nRollnumber = {main_list[i].rollnumber}"
                            )
                            file4 = open("test.txt", "w")
                            file4.write(update_data())
                            file4.close()
