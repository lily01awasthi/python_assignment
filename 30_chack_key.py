"""30. Write a Python script to check whether a given key already exists in a 
dictionary. """
def check_key(dict,key):
    if key in dict:
        print("key already exists.")
    else:
        print("this is a new key")
dict={1:"apple",2:"ball",3:"cat",4:"dog"}
key="ball"
check_key(dict,key)

