def doubled(lst):
    for item in lst:
        print(item * 2)
        
lst = [1,2,3]
print(doubled(lst)) 

# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # When we print the items, do we need a specific format?
    # Do we need to return anything from the function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes a list as input
    # Iterate through each item in the list and double it
    # print the doubled item
# 3. Translate each sub-problem into pseudocode:
    # func(list):
    #     for each item in list:
    #         double_item = item * 2
    #         print(double_item)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def doubled(lst):
    for item in lst:
        double_item = item * 2
        print(double_item)