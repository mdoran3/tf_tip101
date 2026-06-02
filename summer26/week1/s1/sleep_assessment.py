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