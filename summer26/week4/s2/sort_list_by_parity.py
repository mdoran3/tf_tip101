##################################
# Problem 3: Sort List by Parity #
##################################

'''
Write a function sort_array_by_parity() that takes in a list of 
integers nums where half of the integers are odd, and the other 
half are even. The function sorts the list so that whenever nums[i] 
is odd, i is odd and whenever nums[i] is even, i is even. The function 
returns the list in any order that satisfies the condition.
'''

### U - Understand
#   Since half the integers are even and half are odd, does that guarantee every
#       even index has a matching odd index to swap with if needed?
#   Does the relative order of even numbers among even indices (or odd among odd)
#       matter, or just that each lands in a same-parity index?

### P - Plan
'''
Use two pointers — one starting at index 0 (even lane) and one at index 1 (odd lane),
each advancing by 2 to stay in their lane.

    Walk the even pointer forward (by 2) until we find an odd number sitting at an even index.
    Walk the odd pointer forward (by 2) until we find an even number sitting at an odd index.
    Swap those two misplaced elements.
    Repeat until both pointers go out of bounds.
    Return the modified list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
even = 0
odd = 1

while even < len(nums) and odd < len(nums):
    while even < len(nums) and nums[even] is even:
        even += 2
    while odd < len(nums) and nums[odd] is odd:
        odd += 2
    if both pointers still in bounds:
        swap nums[even] and nums[odd]

return nums
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def sort_array_by_parity(nums):
    even, odd = 0, 1
    while even < len(nums) and odd < len(nums):
        while even < len(nums) and nums[even] % 2 == 0:
            even += 2
        while odd < len(nums) and nums[odd] % 2 == 1:
            odd += 2
        if even < len(nums) and odd < len(nums):
            nums[even], nums[odd] = nums[odd], nums[even]
    return nums


nums = [4,2,5,7]
nums2 = [2,3]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

'''
Example Output:

[4,5,2,7]
# [2,7,4,5], [2,7,4,5], [4,7,2,5] also works
[2,3]
'''