"""24. Write a Python program to clone or copy a list."""

no_of_items=int(input("enter the no of items you want in a list: "))
inp_list=[]
for i in range(no_of_items):
    inp=input("enter the list items of integers : ")
    inp_list.append(inp)
print(inp_list)
copy_list=[]
copy_list=inp_list.copy()
print(f"copy of list in copy_list:{copy_list}")