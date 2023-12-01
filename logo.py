def logo_C():
    rows = int(input("enter the number of rows : "))
    rows_3 = rows * 3

    for i in range(1, rows_3 + 1):
        if i <= rows:
            for c in range(rows_3):
                print("@ ", end="")
        if i > rows and i <= (2 * rows):
            for c in range(rows + 1):
                print("@ ", end="")
        if i > (2 * rows):
            for c in range(rows_3):
                print("@ ", end="")
        print()


def logo_E():
    rows = int(input("enter the number of rows : "))
    rows_3 = rows * 3

    for i in range(1, rows_3 + 1):
        if i <= rows:
            for c in range(rows_3):
                print("@ ", end="")
        if i > rows and i <= (2 * rows):
            for c in range(rows + 1):
                print("@ ", end="")
        if i > (2 * rows):
            for c in range(rows_3):
                print("@ ", end="")
        print()

    for i in range(1, rows * 2):
        if i <= rows:
            for c in range(rows + 1):
                print("@ ", end="")
        if i > rows and i <= (2 * rows):
            for c in range(rows_3):
                print("@ ", end="")
        print()


def logo_H():
    rows = 9
    rows_3 = rows * 3
    k = 0
    for i in range(1, rows):
        for space in range(1, (rows - 1 - i) + 1):
            print(end=" ")
        while k != (2 * i - 1):
            print("@", end="")
            k += 1
        k = 0
        print()
    for i in range(1, rows + 7):
        while True:
            print(end="   ")
            if i <= (rows - 4):
                for c in range(rows):
                    print("@", end="")
                for c in range(rows):
                    print(" ", end="")
                for c in range(rows):
                    print("@", end="")
            if i > (rows - 4) and i <= (2 * (rows - 4)):
                for c in range(rows_3):
                    print("@", end="")
            if i > (2 * (rows - 4)):
                for c in range(rows):
                    print("@", end="")
                for c in range(rows):
                    print(" ", end="")
                for c in range(rows):
                    print("@", end="")
            print()
            break
    for i in range(rows, 1, -1):
        while True:
            print(end="                  ")
            for space in range(0, (rows - i)):
                print(end=" ")
            while k != (2 * i - 3):
                print("@", end="")
                k += 1
            k = 0
            print()
            break


logo_H()
logo_C()
logo_E()
