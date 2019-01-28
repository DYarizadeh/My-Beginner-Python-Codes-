list = []
swapped = True
num = int(input("How many numbers would you like for me to sort out? "))
for i in range(num) :
    val = float(input("Please enter your numbers: "))
    list.append(val) 
while swapped:
    swapped = False
    for i in range(list(len - 1)):
        if list [i]>list[i+1 ]:
            swapped = True
            list [i], list [i+1]=list [i+1],list
print ("Sorted: ")
print (list)  
