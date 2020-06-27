"""2. Write a Python function to sum all the numbers in a list.Sample List : (8, 2, 3, 0, 7) 
Expected Output : 20 """
def sum_list(lis):
    total_sum=0
    for i in lis:
        total_sum+=i 
    return total_sum
List1 =[8, 2, 3, 0, 7]
total=sum_list(List1)
print(total)