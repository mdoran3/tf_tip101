### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What are we NOT allowed to do in this problem?
    # What are the inputs?
    # What is the output?

### P - Plan
# 2. Write out in plain English what you want to do: 
    #  Our for loop starts at 1 and then only counts to 5 but not inclusive.
    #  We want to be able to inlcude 5 at the end. This is a classic "Off by One" error.
    #  We can fix list by adding one to our terminal condition in the for loop range. 
# 3. Translate each sub-problem into pseudocode:
    #  func(a):
    #      for num in range(1, a + 1):
    #          print( f"{num} blah")

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
    #  def count_mississippi(limit):
    #      for num in range(1, limit + 1):
    #          print( f"{num} mississippi")

# Call the function so that it prints out the following to 
# the console (without calling the function more than once):

def count_mississippi(limit):
    for num in range(1, limit + 1):
        print( f"{num} mississippi")

count_mississippi(5)