"""11. Write a Python program to count the occurrences of each word in a given
sentence."""
inp=input("enter your sentence: ")
inp_list=inp.split()
inp_dict={}
for i in inp_list:
    if i in inp_dict:
        inp_dict[i]+=1
    else:
        inp_dict[i]=1
print(inp_dict)