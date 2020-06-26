"""8. Write a Python program to remove the nth index character from a nonempty string."""
inp=input("enter a non empty string: ")
index = int(input("enter the index of the character you want to remove: "))
print(inp[0:index] + inp[index+1:])