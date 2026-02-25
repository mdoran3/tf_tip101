# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What are the input parameters of the function?
    # How many lists do we return?
    # Do we need to create any ne dicts?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in two dicts as params
    # Iterate through the restock dict and check if it already exists in the inventory list
    # If it does, add the value of the restock dict to the inventory dict
    # If it doesn't, add the key and value to the inventory dict
    # Return the inventory dict 
# 3. Translate each sub-problem into pseudocode:
    # func(inventory, restock):
        # for key in restock:
            # if key in inventory:
                # inventory[key] += restock[key]
            # else:
                # inventory[key] = restock[key]
        # return inventory

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def restock_inventory(inventory, restock):
    for key in restock:
        if key in inventory:
            inventory[key] += restock[key]
        else:
            inventory[key] = restock[key]
    return inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))
