"""16. Write a Python program to sum all the items in a list. """
no_of_items=int(input("enter the no of items you want in a list: "))
inp_list=[]
for i in range(no_of_items):
    inp=int(input("enter the list items of integers : "))
    inp_list.append(inp)
sum=0
for i in inp_list:
    sum=sum+i
print(sum)