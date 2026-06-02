# Write a function index_to_value_map() that takes in a list lst 
# and returns a dictionary that maps the index of each element in 
# lst to its value.

def index_to_value_map(lst):
    fruits = {}
    for i in range(0, len(lst)):
        fruits[i] = lst[i]
    return fruits

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))