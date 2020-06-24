"""4. Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
inp= input("enter your string: ")
new_inp=inp.split(" ")
str1=new_inp[0]
str2=new_inp[1]
new_str1=str1.replace(str1[0],str2[0])
new_str2=str2.replace(str2[0],str1[0])
print(new_str1,new_str2)