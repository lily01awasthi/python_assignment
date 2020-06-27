"""26. Write a Python program to insert a given string at the beginning of all items in 
a list."""

no_of_items=int(input("enter the no of items you want in a list: "))
add_string=input("enter the string to add: ")
inp_list=[]
for i in range(no_of_items):
    inp=input("enter the list items: ")
    inp_list.append(inp)
print(inp_list)
new_list=[]
for i in inp_list:
    i=add_string+i
    new_list.append(i)
print(new_list)