"""1. Write a Python function to find the Max of three numbers."""

def find_max(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is largest")
        else:
            print(f"{c} is largest")
    elif b>c:
        print(f"{b} is largest")
    else:
        print(f"{c} is largest")
find_max(21,34,54)
