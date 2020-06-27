"""43. Write a Python program to remove an item from a tuple."""
sample_tuple=("hello","lily","101")
sample_list=list(sample_tuple)
item=input("enter the item you want to remove: ")
if item in sample_list:
    sample_list.remove(item)
sample_tuple=tuple(sample_list)
print(sample_tuple)