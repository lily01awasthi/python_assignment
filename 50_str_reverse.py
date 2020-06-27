"""4. Write a Python program to reverse a string. 
Sample String : "1234abcd" 
Expected Output : "dcba4321" """

def reverse_str(str):
    new_str=""
    for i in range(len(str)):
        new_str=new_str+str[-(i+1)]
    return(new_str)
str="1234abcd"
reverse_string=reverse_str(str)
print(reverse_string)