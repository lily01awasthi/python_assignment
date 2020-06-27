"""38. Write a Python program to remove a key from a dictionary. """
sample_dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 
13: 169, 14: 196, 15: 225}
key=int(input("enter the key you want to remove: "))
del sample_dict[key]
print(sample_dict)