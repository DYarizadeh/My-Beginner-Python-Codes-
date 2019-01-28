year = int(input("Enter a year: "))
if (year < 1582):
    print ("This year is excluded from the leap year peramaters (must be before 1582).")
elif (year % 4 != 0):
    print ("Common Year")
elif (year % 100 != 0):
    print ("Leap Year")
elif (year % 400 != 0):
    print ("Common Year")
else: 
    print ("Leap Year")
