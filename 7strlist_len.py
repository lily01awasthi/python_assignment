"""7. Write a Python function that takes a list of words and returns the length of the
longest one.
"""
def longeststr(usr_list):
    temp=""
    for i in usr_list:
        if(len(i)>len(temp)):
            temp=i
    return (temp,len(temp))

user_list=input("enter the list elements separated nt space: ")
user_list=user_list.split(" ")
word,maxlen=longeststr(user_list)
print(f"maximum length word is: {word} with length: {maxlen} ")
