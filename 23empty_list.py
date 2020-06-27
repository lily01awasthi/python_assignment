"""23. Write a Python program to check a list is empty or not. """
def check_list(lis):
    if len(lis)!=0:
        print("list is not empty")
    else:
        print("list is empty")
no_of_items=int(input("enter the no of items you want in a list: "))
inp_list=[]
for i in range(no_of_items):
    inp=input("enter the list items of integers : ")
    inp_list.append(inp)
print(inp_list)
check_list(inp_list)
