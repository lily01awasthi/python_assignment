"""6. Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""
inp=input("enter your string: ")
index_not=inp.find("not")
index_poor=inp.find("poor")
if"not" in inp:
    if "poor" in inp :
        if index_not<index_poor:
            inp=inp.replace(inp[index_not:index_poor+4],"good")
            print(inp)
else:
    print(inp)
