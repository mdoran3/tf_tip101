# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What will the time complexity of this function be?
    # What are we returning if the key doesn't exist in the dictionary?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a fun that takes in a dictionary and a key
    # Check if the key exists in the dictionary
    # If it does, return the key and value in a string format
    # If it doesn't, return "key not found"

# 3. Translate each sub-problem into pseudocode:
    # func(dict, key):
        # if key in dict:
            # print(f"Key {key}")
            # print(f"Value {dict[key]}")
        # else:
            # return "That pair does not exist!"

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def print_pair(dict, key):
    if key in dict:
        print(f"Key: {key}")
        print(f"Value: {dict[key]}")
    if key not in dict:
        print("That pair does not exist!")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")