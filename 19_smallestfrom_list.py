"""19. Write a Python program to get the smallest number from a list. """
no_of_items=int(input("enter the no of items you want in a list: "))
inp_list=[]
for i in range(no_of_items):
    inp=int(input("enter the list items of integers : "))
    inp_list.append(inp)
print(inp_list)
inp_list.sort()
print(f"smallest item in the list is:{inp_list[0]} ")