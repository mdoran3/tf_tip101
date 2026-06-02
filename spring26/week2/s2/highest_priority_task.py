# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Is there a specific variable we should keep track of here?
    # What is the asymptotic time complexity of our function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in a dict as a parameter
    # Create a variable to keep track of the highest priority and set it to 0 or even better, -inf
    # Iterate through each element in the dict and see if its priority is higher than the current and update accordingly
    # Remove the highest priority task from the dict and return it
# 3. Translate each sub-problem into pseudocode:
    # func(dict):
        # highest_priority = -inf
        # for task in dict:
            # if dict[task] > highest_priority:
                # highest_priority = dict[task]
                # highest_task = task
        # del dict[highest_task]
        # return highest_task

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def highest_priority_task(tasks):
    highest_priority = float("-inf")
    highest_task = ""
    for task in tasks:
        if tasks[task] > highest_priority:
            highest_priority = tasks[task]
            highest_task = task
        elif tasks[task] == highest_priority and task > highest_task:
            highest_priority = tasks[task]
            highest_task = task
    del tasks[highest_task]
    return highest_task
    
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (highest_priority_task(tasks))
print(perform_task)

perform_task = (highest_priority_task(tasks))
print(perform_task)

perform_task = (highest_priority_task(tasks))
print(perform_task)

print(tasks)