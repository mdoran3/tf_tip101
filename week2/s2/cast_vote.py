# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What inputs are being passed as parameters to our function?
    # What is the expected output of our function?
    # Do we need to create a new dict?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in a dict and a string as parameters
    # Check if the candidate string that was passed in is a key in the dict
    # If it is, add 1 to the value of that key in the dict
    # If it is not, add the candidate string as a key to the dict with a value of 1
    # Return the dict
# 3. Translate each sub-problem into pseudocode:
    # func(dict, candidate):
        # if candidate in dict:
            # dict[candidate] += 1
        # else:
            # dict[candidate] = 1
        # return dict

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)