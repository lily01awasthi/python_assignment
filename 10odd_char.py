"""10. Write a Python program to remove the characters which have odd index
values of a given string. """

inp=input("enter a non empty string: ")
temp=""
for i in inp:
    if inp.find(i)%2==0:
        temp=temp+i
print(temp)

#incase of repeated character in a word it takes the first index found.?????????