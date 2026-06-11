# Write a function string_to_integer_mapping() that takes in a string 
# of digits s as a parameter and returns a list where each element is 
# the integer value of the corresponding digit in the string.

def string_to_integer_mapping(s):
    new_list = []
    for char in s:
        new_char = int(char)
        new_list.append(new_char)
    return new_list


# Example Input: 
s="12345"
print(string_to_integer_mapping(s))

# Example Output: [1, 2, 3, 4, 5]