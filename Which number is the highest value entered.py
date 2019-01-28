max = -999999
counter = 0

while True:
    number = int(input("Enter a value: "))
    if number == -1:
        break
    if number>max:
        max = number
        counter += 1
    if counter:
        print("The largest value is ", max)
    else:
        print("Are you kidding? You haven't even entered any value!") 
