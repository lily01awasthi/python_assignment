"""1. Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
inp=input("enter your string:")
str_dict = {}
for i in inp:
    if i in str_dict:
        continue
    else:
        str_dict[i]=inp.count(i)
print(str_dict)

