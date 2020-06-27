"""10. Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
Expected Result : [2, 4, 6, 8] """

def check_even(lis):
    new_lis=[]
    for num in lis:
        if (num%2)==0:
            new_lis.append(num)
    return(new_lis)
Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(check_even(Sample_List))