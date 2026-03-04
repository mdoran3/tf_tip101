def doubled(lst):
    return [item * 2 for item in lst]

lst = [1,2,3]
print(doubled(lst))

# Tech Fellow Task Instructions 
# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What does the function take in as input?
    # What does the function output and in what format?

### P - Plan
# 2. Write out in plain English what you want to do: 
  # Write a func that takes a list as input
    # Iterate through each item in the list and double it
    # append the doubled item to a new list
    # return the new list
# 3. Translate each sub-problem into pseudocode:
    # func(list):
    #     new_list = []
    #     for each item in list:
    #         double_item = item * 2
    #         append double_item to new_list
    #     return new_list


### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def doubled(lst):
    new_lst = []
    for item in lst:
        double_item = item * 2
        new_lst.append(double_item)
    return new_lst