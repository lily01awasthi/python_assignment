"""9. Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.
"""
inp=input("enter a non empty string: ")
print(inp[-1]+inp[1:-1]+inp[0])