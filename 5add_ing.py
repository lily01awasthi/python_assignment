"""5. Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
inp = input("enter your string: ")
if len(inp)<3:
    print(inp)
elif inp[-3:]=="ing":
    inp=inp+"ly"
    print(inp)
else:
    inp=inp+"ing"
    print(inp)