"""9. Write a Python function that takes a number as a parameter and check the 
number is prime or not. 
Note : A prime number (or a prime) is a natural number greater than 1 and that 
has no positive divisors other than 1 and itself."""

def check_prime(num):
    if(num>1):
        for i in range(2,num):
            if (num%i)==0:
                print("not prime")
                break
        else:
            print("number is prime")
    else:
        print("not prime")
        
inp=int(input("enter the number to check: "))
check_prime(inp)