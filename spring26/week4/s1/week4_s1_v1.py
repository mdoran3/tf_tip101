# PROBLEM 1: PRIME NUMBER

# Write a function is_prime() that takes in a positive integer n and 
# returns True if it is a prime number and False otherwise. A prime 
# number is a number greater than 1 that has no positive divisors other 
# than 1 and itself.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # INPUT: an integer
    # OUTPUT: A boolean value
    # What makes a number prime?
    # Why are prime numbers important in CS?
    # Should be use a loop?
    # What mathematical operator could be helpful in this problem?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create while loop and decrement down from one below the number until one above number
    # run a modulus
    # if mod == 0 return True
    # if mod never == 0 return False

# 3. Translate each sub-problem into pseudocode:
    # i = n-1
    # while i is greater than 1
        # if n mod i == 0 then it is true
        # else i -+ 1
    # return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_prime(n):
    i = n -1
    while i > 1:
        if n % i == 0:
            return False
        else:
            i -= 1
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))


# PROBLEM 2: TWO-POINTER REVERSE LIST

# Write a function reverse_list() that takes in a list lst and returns 
# elements of the list in reverse order. The list should be reversed 
# in-place without using list slicing (e.g. lst[::-1]).

# Instead, use the two-pointer approach, which is a common technique 
# in which we initialize two variables (also called a pointer in this 
# context) to track different indices or places in a list or string,
# then moves the pointers to point at new indices based on certain 
# conditions. In the most common variation of the two-pointer approach, 
# we initialize one variable to point at the beginning of a list and a 
# second variable/pointer to point at the end of list. We then shift 
# the pointers to move inwards through the list towards each other,
# until our problem is solved or the pointers reach the opposite ends 
# of the list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # INPUT: a list
    # OUTPUT: the same list but reversed
    # Why would we use two pointers to reverse a list?
    # Where do we start the two pointers at?
    # What is the space complexity of this algo?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create two pointer variables - one for the front of the list and one for the end
    # Use a while loop and swap front  and end elements of list until the pointers collide

# 3. Translate each sub-problem into pseudocode:
    # pointer1 = 0
    # pointer2 = len(list) -1
    # while pointer1 less than pointer two:
        # element of list at pointer1 with element of list at pointer2
        # increment pointer1
        # decrement pointer2
    # return the list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def reverse_list(lst):
    front = 0
    back = len(lst) - 1

    while front < back:
        temp = lst[front]
        lst[front] = lst[back]
        lst[back] = temp
        front += 1
        back -= 1
    return lst

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([1, 2, 3, 4, 5, 6]))


# PROBLEM 3: EVALUATING SOLUTIONS

# The reverse_list() problem can also be solved without using the two 
# pointer technique (as you may have seen it in previous units)! Evaluate 
# the time and space complexity of your two-pointer solution.

# Then, evaluate the time and space of the following solution:

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is asymptotic time complexities and how are they noted?
    # What is space complexity?
    # What are considered some of the best times and worst times?

### P - Plan
# 2. Write out in plain English what you want to do: 

    # ALGO 1:
        # Time Complexity: O(n) + O(n) = O(n)
            # List is iterated through once while slicing
            # List is iterated through againt to put back into original list
            # Time complexities are not concerned with factors so => O(n)
        # Space Complexity: O(n)
            # A new list, reverse_list, is created with n elements, so => O(n)

    # ALGO 2
        # Time Complexity: O(n/2) = O(n)
            # With two pointers, list is iterated through n/2 times
            # Time complexity is not concerned with factors so O(n/2) => O(n)
        # Space Complexity: O(1)
            # The list is reversed by operating on the original list and no copy is made

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# ALGO 1
def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]

# ALGO 2
def reverse_list(lst):
    front = 0
    back = len(lst) - 1

    while front < back:
        temp = lst[front]
        lst[front] = lst[back]
        lst[back] = temp
        front += 1
        back -= 1
    return lst


# PROBLEM 4: MORE EVEN INTEGERS

# Write a function sort_list_by_parity() that takes in an integer 
# list nums as a parameter and moves all the even integers at the 
# beginning of the list followed by all the odd integers. The function 
# returns any list that satisfies this condition.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Can we use the two pointer method in the example?
    # Is there a way to do this with O(1) space complexity and O(n) time complexity?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a front and back pointer
    # Create a while loop until front is greater than back pointer
    # Check if front and back are evens and/or odds
    # Swap elements if necessary and adjust the pointer positon

# 3. Translate each sub-problem into pseudocode:
    # Edge case: if len(list) less than 2:
        # return list
    # front: list[0]
    # back: len(list) - 1
    # while front < back
        # if front element even and back element odd
            # increment fron and decrement back
            # continue
        # elif front even and back even
            # increment front
        # elif front odd and back odd
            # decrement back
        # else:
            # swap elements in list
            # increment front
            # decrement back
    # return list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def sort_array_by_parity(nums):
    if len(nums) < 2:
        return nums

    front = 0
    back = len(nums) - 1

    while front < back:
        if nums[front] % 2 == 0 and nums[back] % 2 != 0:
            front += 1
            back -= 1
        elif nums[front] % 2 == 0 and nums[back] % 2 == 0:
            front += 1
        elif nums[front] % 2 != 0 and nums[back] % 2 != 0:
            back -= 1
        else:
            temp = nums[front]
            nums[front] = nums[back]
            nums[back] = temp
            front += 1
            back -= 1

    return nums    

nums = [3,1,2,4,9,10,6,5]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

# PROBLEM 5: PALINDROME

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

# PROBLEM 6: REMOVE DUPLICATES WITH O(1)

# Write a function remove_duplicates() that takes in a sorted list of 
# integers nums as a parameter and removes the duplicates in-place such 
# that each element appears only once. Do not allocate extra space for 
# another array; you must do this by modifying the input list with O(1) 
# extra memory. The function returns the new length of the list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is a helpful pytong function we can use to remove an element?
    # Can we use two pointers? Where might we point them?

### P - Plan
# 2. Write out in plain English what you want to do: 

# 3. Translate each sub-problem into pseudocode:

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def remove_duplicates(nums):
    pos = 1
    while pos < len(nums):
        if nums[pos] == nums[pos-1]:
            del nums[pos]
        else: 
            pos += 1
    return len(nums)

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list