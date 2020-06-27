"""20. Write a Python program to find intersection of two given arrays using 
Lambda. """
a=[1,3,4,6,7,8,9]
b=[4,6,7,9,2,3,5,6,3]
get_intersection=lambda x,y:list(set(x).intersection(set(y)))
print(get_intersection(a,b))