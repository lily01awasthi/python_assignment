"""3. Write a Python function to multiply all the numbers in a list. 
Sample List : (8, 2, 3, -1, 7) 
Expected Output : -336 """
def mul_list(lis):
    total_mul=1
    for i in lis:
        total_mul*=i 
    return total_mul
List1 =[8, 2, 3, -1, 7]
total=mul_list(List1)
print(total)