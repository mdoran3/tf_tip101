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