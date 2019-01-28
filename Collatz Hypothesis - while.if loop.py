steps = 0 
c0 = int(input("Enter a number: "))
while c0 != 1:  
    if c0 % 2 == 0: 
        c0 = c0/2
    elif c0 % 2 == 1: 
        c0 = 3 * c0 + 1
    print (c0, " ", end = "")
    steps += 1 
print (c0, "steps=",steps)