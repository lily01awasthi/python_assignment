"""19. Write a Python program to create Fibonacci series upto n using Lambda."""
num=int(input("enter a number: "))
lis=[]
for i in range(num+1):
    lis.append(i)
get_Fibonacci=lambda num:num if num<=1 else get_Fibonacci(num-1)+get_Fibonacci(num-2)
print(list(map(get_Fibonacci,lis)))
