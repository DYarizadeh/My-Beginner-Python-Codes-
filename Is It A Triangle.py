##def IsItATriangle(a,b,c):
##    return a + b > c and b + c > a and c + a <=b
##print(IsItATriangle(1,1,1))
##print(IsItATriangle(3,7,4))

##def IsItATriangle(a,b,c):
##    if a + b <= c or b + c <= a or c + a <= b:
##        return False
##    return True
##print (IsItATriangle(1,1,1))
##print (IsItATriangle(3,7,4))

##def IsItATriangle(a,b,c):
##    return a + b > c and b + c > a and c + a <=b
##a=float(input("First side's length?"))
##b=float(input("Second side's lenght?"))
##c=float(input("Third side's lenght?"))
##if IsItATriangle(a,b,c):
##    print("Congrats - it is a triangle!")
##else:
##    print("Sorry, it won't be a triangle")
##


def IsItATriangle(a,b,c):
    return a + b > c and b + c > a and c + a <=b
def IsItRightTriangle(a,b,c):
    if c > a and c > b:
        return c**2 == a**2 and b**2
    if a > b and a > c:
        return a**2 == b**2 + c**2
    return a**2 == b**2 + c**2 
print (IsItRightTriangle(5,3,4))
print (IsItRightTriangle(3,7,4))
print (IsItATriangle(3,7,4))
