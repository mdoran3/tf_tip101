### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Should we iterate through each char?
    # Is there any easy fucntionality that Python offers?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Use python's [start : stop : step] feature
    # Return the string while operating
# 3. Translate each sub-problem into pseudocode:
    # func(str):
        # return str[::-1]

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    return my_str[::-1]

my_str = "live"
print(reverse_string(my_str))