"""18. Write a Python program to check whether a given string is number or not 
using Lambda."""
str="123"
is_number=lambda str:bool(int(str))

try:
    is_number(str)
    print("the given string is integer")
except:
    print("the given string is not an inteeger")