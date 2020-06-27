"""19. Write a Python program to create Fibonacci series upto n using Lambda."""
num=int(input("enter a number: "))
get_Fibonacci=lambda i:i+(i+1)
count=0
fibo_lis=[0]
while(count<num):
    x=get_Fibonacci(count)
    fibo_lis.append(x)
    count+=1
print(fibo_lis)