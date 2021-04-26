#CS362 HW3 Q3
#934-371-471 Yuna Oh
#Input year and press enter. Then Output will be printed.

class MyError(Exception):
    pass

def number_chk(yr):
    if not yr.isdecimal():
        raise MyError()

y = input('Input year : ')

try:
    number_chk(y)
except MyError:
    print("It's not a number")
    exit()

year = int(y)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " is a common year.")
    else:
        print(str(year) + " is a leap year.")
else:
    print(str(year) + " is a common year.")
