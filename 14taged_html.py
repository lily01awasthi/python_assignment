"""14. Write a Python function to create the HTML string with tags around the
word(s).Sample function and result :

add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""
def add_tags(i,text):
    print(f"<{i}>{text}</{i}> ")
inp=input("enter your text: ")
tag=input("enter your tag: ")
add_tags(tag,inp)