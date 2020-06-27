"""20. Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given list of 
strings.Sample List : ['abc', 'xyz', 'aba', '1221'] 
Expected Result : 2 
"""
no_of_items=int(input("enter the no of items you want in a list: "))
inp_list=[]
for i in range(no_of_items):
    inp=input("enter the list items of string : ")
    inp_list.append(inp)
count=0
for i in inp_list:
    if len(i)>2:
        if i[0]==i[-1]:
            count+=1
print(count)