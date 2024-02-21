my_set={"apple", "banana", "cherry", "mango", "orange"}
print (my_set)

print (len(my_set))

size_set = int(len(my_set))
user_input = int(input ('Your Number: '))
if (user_input>size_set):
    print ('Add your choice: ')
    user_choice=input()
    my_set.add(user_choice)
    print (my_set)
else:
    # update set
    other_set={'plantain', 'grapes'}
    my_set.update(other_set)
    print (my_set)
for val in my_set:
    print (val)
    