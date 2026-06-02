# Write a function first_palindrome() that takes in a list of strings words 
# as a parameter and returns the first palindromic string in the list. 
# A string is palindromic if it reads the same forward and backward. If there 
# is no such string, return an empty string ""

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Can we use a two pointer trick again?
    # What if multiple words are palindromes?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Use for loop to iterate through each word in list
    # Create a pointer front = 0 and pointer back = len(word) -1
    # Create a while loop in the for loop - while front < back
    # if front and back are equal, increment front and decrement back
    # then check if front is great than or equal to back and if so, return word
    # else break out of while and let use iterate to next string in the words list

# 3. Translate each sub-problem into pseudocode:
    # for word in words
        # front = 0
        # back = len(word) -1
        # While front is less than back:
            # if front equals back:
                # increment front
                # decrement back
                # if front greater than or equal to back:
                    # return word
            # else:
                # break

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def first_palindrome(words):
    for word in words:
        front = 0
        back = len(word) - 1
        while front < back:
            if word[front] == word[back]:
                front += 1
                back -= 1
                if front >= back:
                    return word
            else:
                break
    return None

words = ["abc", "car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)