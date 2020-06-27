"""7. Write a Python function that accepts a string and calculate the number of 
upper case letters and lower case letters. 
Sample String : 'The quick Brow Fox' 
Expected Output : 
No. of Upper case characters : 3 
No. of Lower case Characters : 12 """

def count_case(data):
    upper_count=0
    lower_count=0
    for i in range(len(data)):
        if data[i].isupper():
            upper_count+=1
        elif data[i].islower():
            lower_count+=1
    print(f"No. of Upper case characters :{upper_count}")
    print(f"NO. of Lower case characters :{lower_count} ")

str=input("enter the string: ")
count_case(str)