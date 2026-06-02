### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of loop should we use?
    # Do we need to iterate through every second or moment of poisoning?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Set the time of damage to 0 
    # Create a for loop with range of length of the time series -1
    # Find the difference between the current element in the time series and the next one
    # Run the built in minimum function between the difference and the duration parameter
    # Add this result to your damage
    # Outside of the loop add duration to the damage since nothing else will conflcit with it
    # Return the damage

# 3. Translate each sub-problem into pseudocode:
    # func(list, int)
        # damage = 0
        # for i in range of length of list -1 
            # diff = list[i+1] - list[i]
            # min(diff, int)
            # add min to damage
        # add int to damage
        # return damage 

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# In the game League of Legends, Teemo attacks his enemy Ashe with poison 
# arrows. Write a function find_poisoned_duration() that takes in two 
# parameters: time_series (the time at which Teemo's attacks hits Ashe) '
# 'and time_duration (the duration of the poisoning effect). The function '
# 'returns the total time that Ashe is in a poisoned condition.time_series '
# 'is a list of integers that represents the times at which Teemo attacks '
# 'and makes Ashe poisoned for the exact time_duration.If Teemo hits Ashe '
# 'while she is still poisoned, the poison's duration starts over. For 
# example, if Teemo attacks at times 1 and 4 for 3 seconds, the states at 
# each time would be:

# This means that the total time that Ashe is in a poisoned condition is 5.

def find_poisoned_duration(time_series, duration):
    if not time_series:
        return 0
    damage = 0
    for i in range(len(time_series) - 1):
        diff = time_series[i + 1] - time_series[i]
        damage += min(diff - 1, duration)
    damage += duration
    return damage

time_series = [1,4, 9]
damage = find_poisoned_duration(time_series, 3)
print(damage)