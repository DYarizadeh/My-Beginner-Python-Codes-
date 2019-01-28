#step 1 
Beatles = []
print("Step 1:", Beatles)
#step 2 
Beatles.append ('John Lennon')
Beatles.append ('Paul McCartney')
Beatles.append ('George Harrison')
print("Step 2:", Beatles)

#step 3
for i in range (2): 
   Beatles.append(input("Enter Stu Stucliffe and then Pete Best: "))
print("Step 3:", Beatles)

# step 4
del Beatles[-1]
del Beatles[-1]
print("Step 4:", Beatles)

Beatles.insert (0, 'Ringo Starr')
# step 5
print("Step 5:", Beatles)

print("The Fab",len(Beatles))
