"""15. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""
def insert_sting_middle(braces,text):
    result=braces[0:len(braces)//2]+text+braces[len(braces)//2:]
    print(result)


inp=input("enter your braces: ")
text=input("enter the string to insert: ")
insert_sting_middle(inp,text)
