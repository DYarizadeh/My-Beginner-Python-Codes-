def isitatriangle(a,b,c):
    return a + b > c and b + c > a and c + a <= b

def Heron (a,b,c):
    p = (a + b + c)/2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def FieldOfTriangle(a,b,c):
    if isitatriangle(a,b,c):
        print ("It is a triangle and here is it's field")
    else:
        print ("It is not a triangle but here is the calculation run \
through Heron's forumla") 
    return Heron (a,b,c)

print(FieldOfTriangle(1.0,1.0,2.0**.5))
