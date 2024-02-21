mylist= ["apple", "banana", "cherry", "mango", "orange"]
print ('my firt list is ', mylist)

get_list= list(("apple", "banana", "cherry", "mango", "orange", 9, 8))
print ('My second list is', get_list)

user_choice=int(input("Enter your fruit choice:" ))

if (user_choice<8):
    print ('Your Choice is: ', get_list[user_choice])
else:
    print ('Your Choice is invalid. Pls try again')

#range in list is def by start index:end index, if there is no start index,
    # if will print from the begining of the end index and vice versa
print (get_list[2:])

#add new value to list using append
get_list.append('pawpaw')
print(get_list)

# to add more than one value to a list
get_list.extend(['coconut', 'baobab', 'berry'])
print(get_list)

#insert a value at a particular location
get_list.insert(2, 'apple')
print(get_list)

# to delete an item 

get_list.remove(9)

# to delete using item index
get_list.pop (6)

print(get_list)

# sort a list

get_list.sort()
print (get_list)









