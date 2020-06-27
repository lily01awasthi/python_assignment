"""15. Write a Python program to filter a list of integers using Lambda."""
sample_lis=[1,2,3,4,5,6,7]
integer_filter=filter(lambda lis: lis%2==0,sample_lis)
print(list(integer_filter))