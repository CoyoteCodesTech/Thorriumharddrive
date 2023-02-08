import random

integer = 0
times_looped = 1

print()
goalNum = int(input("What is your favorite large integer? "))
print()

try:
    assert (
        len(str(goalNum)) >= 3
    ), "ValueError: type int() has less than three (3) digits."
except AssertionError as err:
    print(err)
    quit()


while integer != goalNum:
    integer = random.randint(0, goalNum)
    print(integer)
    if integer == goalNum:
        print()
        if times_looped == goalNum:
            print("This program ran exactly", goalNum, "times!")
        elif times_looped == 1:
            print("This program only ran once!")
        else:
            print("This program ran", times_looped, "times.")
    times_looped += 1
