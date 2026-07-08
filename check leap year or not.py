year = int(input("enter the year"))
if (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0):
    print("given yera is a leap year")
else:
    print("given year is not a leap year")
