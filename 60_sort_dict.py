"""14. Write a Python program to sort a list of dictionaries using Lambda. """
sample_list=[{"fruit":"apple","price":120},{"fruit":"orange","price":60},{"fruit":"mango","price":100}]
fetch_price=lambda x:x["price"]
print(sorted(sample_list,key=fetch_price))