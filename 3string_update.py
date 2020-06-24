"""3. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
inp=input("enter your string: ")
for i in inp[1::1]:
    if i==inp[0]:
        new_str=inp[0]+inp[1:].replace(i,"$")
print(new_str)

