"""40. Write a Python program to add an item in a tuple."""
sample_tuple=("hello","lily","101")
sample_list=list(sample_tuple)
sample_list.append("i@m added_item")
sample_tuple=tuple(sample_list)
print(sample_tuple)