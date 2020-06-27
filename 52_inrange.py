"""6. Write a Python function to check whether a number is in a given range. """
def in_range(frm,to,num):
    if frm<num<to:
        print("given number is in given range")
    else:
        print("given number is not in given range")
num=int(input("enter the number: "))
frm=int(input("enter the initial range: "))
to=int(input("enter the final range: "))
in_range(frm,to,num)