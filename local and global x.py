def bmi():
    x = float(input("What is the height in meters? "))
    y = float(input("What is weight in kg? "))
    body_mass = y/x**2
    print (body_mass)
bmi()
