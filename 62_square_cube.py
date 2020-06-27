"""16. Write a Python program to square and cube every number in a given list of 
integers using Lambda"""
sample_list=[1,2,4,5,7,21]
square_map=map(lambda num:num*num,sample_list)
print(f"square_list:{list(square_map)}")
cube_map=map(lambda num:num*num*num,sample_list)
print(f"cube_list:{list(cube_map)}")