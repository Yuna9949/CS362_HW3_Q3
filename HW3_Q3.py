#CS362 HW3 Q3
#934-371-471 Yuna Oh
#Input year and press enter. Then Output will be printed.

year = int(input('Input year : '))

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
