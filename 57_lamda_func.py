"""11. Write a Python program to create a lambda function that adds 15 to a given 
number passed in as an argument, also create a lambda function that multiplies 
argument x with argument y and print the result."""

total_sum=lambda num:num+15
print(total_sum(5))

total_mul=lambda x,y:x*y
print(total_mul(4,6))