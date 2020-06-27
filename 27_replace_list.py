"""27. Write a Python program to replace the last element in a list with another list. 
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8] 
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8] """

def get_list():
    no_of_items=int(input("enter the no of items you want in list: "))
    inp_list=[]
    for i in range(no_of_items):
        inp=input("enter the list items: ")
        inp_list.append(inp)
    print(inp_list)
    return inp_list
print("Enter your first list:")
first_list=get_list()
print("enter the list you want to replace: ")
second_list=get_list()
first_list.remove(first_list[-1])
first_list.append(second_list)
print(first_list)