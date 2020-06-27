"""25. Write a Python program to check whether all dictionaries in a list are empty or 
not. 
Sample list : [{},{},{}] 
Return value : True 
Sample list : [{1,2},{},{}] 
Return value : False 
"""
def is_empty(lis):
    for i in lis:
        if bool(i):
            print("False")
            return 0
        else:
            continue
    print("True")
Sample_list=[{},{},{}] 
is_empty(Sample_list)
