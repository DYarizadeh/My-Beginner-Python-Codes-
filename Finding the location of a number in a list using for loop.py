list = [1,2,3,4,5,6,7,8,9,10]
tofind = 5
found = False
for i in range (len(list)):
    found = list[i]== tofind
    if found:
        break
if found:
    print ("Element found at index ", i)
else:
    print ("absent") 
