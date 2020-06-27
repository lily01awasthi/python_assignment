"""28. Write a Python script to add a key to a dictionary. 
Sample Dictionary : {0: 10, 1: 20} 
Expected Result : {0: 10, 1: 20, 2: 30} """
inp_dict={}
no_of_items=int(input("enter the no of items you want in the dictionary: "))
for i in range(no_of_items):
    key=input("enter the key you want to add: ")
    value=int(input("enter the value for yur key: "))
    inp_dict[key]=value
print(inp_dict)