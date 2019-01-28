def Factoral():
    n = int(input("Input a number to take the factoral of: "))
    if n < 0:
        return None
    
    product = 1
    for i in range (1,n+1):
        product *= i
        print(i,product)
        
Factoral()

