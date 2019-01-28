# an existing list of numbers hidden in the hat
hat_list = [1, 2, 3, 4, 5]

#change the middle number in the list
hat_list [2] = int(input("Enter a number: ")) 
# deletes the last number in the list 
del hat_list [-1]
#print the lenght of the list
print(len(hat_list))

# printing the list
print(hat_list)

#test the list 
print((hat_list[2] + 7) == sum(hat_list))
