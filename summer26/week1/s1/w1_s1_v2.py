##########################
# Problem 1: Hello User! #
##########################

# Write a function greet_user() that takes in a string name as 
# a parameter and prints "Hello <name>".

# Example Input: Michael
# Example Output: Hello Michael

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is a variable and how do we create one in Python?
#   Python is an interpreted language. What does that mean?

### P - Plan

# 2. Write out in plain English what you want to do: 
#   make a print statement
#   inside the print statment, concatenate a hardcoded string with the parameter variable passed in function. 

# 3. Translate each sub-problem into pseudocode:
#   func(name):
#       print(f"message, {name}!"")
#
#   then make sure to call the function after naming a variable

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def greet_user(name):
    print(f"Hello, {name}!")

name = "Michael"
greet_user(name)



###################################
# Problem 2: Calculate Difference #
###################################

# Write a function difference() that returns the difference between 
# two integers a and b (b should be subtracted from a).

# Example Usage: diff = difference(8, 3)
# Example Output: diff = 5

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What are we returning from the function?
#   How do we print the returned value so we can see it?

### P - Plan
# 2. Write out in plain English what you want to do: 
#     name a new variable to be returned
#     use the parameters passed in the function and subtract a from b 
#     set that equal to the new variable and return it
#
# 3. Translate each sub-problem into pseudocode:
    # func(a, b)
    #     result = a - break
    #     return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def difference(a, b):
    return a - b

a = 8
b = 3
print(difference(a,b))



#################################
# Problem 3: List Concatenation #
#################################

# Given an integer list nums of length n, create a function 
# concatenate_list() that creates and returns a list ans of 
# length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] 
# for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums lists.

# Example Input: [1,2,3,4]
# Example Output: [1,2,3,4,1,2,3,4]

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is concatenation?
#   What does is mean for a list to be concatenated?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   create a new list variable
#   add the parameter to itself with the "+" mathematical operator and set it equal to var
#   return the var

# 3. Translate each sub-problem into pseudocode:
#   func(nums):
#       new_list = nums + nums
# return new_list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def concatenate_list(nums):
    lst = nums + nums
    return lst

nums = [1,2,3,4]
print(concatenate_list(nums))



###############################
# Problem 4: Sleep Assessment #
###############################

# Write a function sleep_assessment() that takes in an integer parameter 
# hours indicating the number of hours the user slept.
# If hours is less than 8, print "Oof, go back to bed!".
# If hours is greater than or equal to 8 and less than or equal to 10, print "You got a good night's rest!".
# If hours is greater than 10, print "You're a sleep prodigy!".

# Example Usage:

# sleep_assessment(10)
# sleep_assessment(4)
# sleep_assessment(12)
# sleep_assessment(9)

# Example Output:

# You got a good night's rest!
# Oof, go back to bed!
# You're a sleep prodigy!
# You got a good night's rest!

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is logic, and specifically, conditional logic in computation?
#   How many logical branches are in this problem?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   Create three conditional logic statements
#       if housrs < 8
#       if hours >= 8 and hours < 10
#       if hours > 10

# 3. Translate each sub-problem into pseudocode:
#   func(hours):
#       if hours < 8:
#           print()
#       if hours >= 8 and hours < 10:
#           print()
#       if hours > 10:
#           print()

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def sleep_assessment(hours):
    if hours < 8:
       print("Oof, go back to bed!")
    if hours >= 8 and hours < 10:
       print("You got a good night's rest!")
    if hours >= 10:  
       print("You're a sleep prodigy!")

sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)



############################
# Problem 5: Calculate Tip #
############################

# Write a function calculate_tip() that takes in a float bill and a string service_quality as parameters.
# If service_quality is "poor", the function should return 10% of the bill value.
# If service_quality is "average", the function should return 15% of the bill value.
# If service_quality is "excellent", the function should return 20% of the bill value.
# If service_quality is any other value, the function should return None.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How many conditinal branches are in this problem?
#   Instead of simply printing statements in each branch, what are we doing instead?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   if service is poor, return the bill * 0.10
#   if service is average, return the bill * 0.15
#   if service is excellent, return the bill * 0.20
#   else, just return None

# 3. Translate each sub-problem into pseudocode:
#   func(bill, service):
#       if service is poor: return bill * 0.10
#       if service is average: return bill * 0.15
#       if service is excellent: return bill * 0.20
#       if service is a different value : return None

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return bill * 0.10
    elif service_quality == "average":
        return bill * 0.15
    elif service_quality == "excellent":
        return bill * 0.20
    else:
        return None


tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)