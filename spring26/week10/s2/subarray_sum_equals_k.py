####################################
# PROBLEM 5: SUBARRAY SUM EQUALS K #
####################################

# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum 
# equals to k.

# A subarray is a contiguous non-empty sequence of 
# elements within an array.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#    - Can nums contain negative integers? (Yes — this rules out a sliding window approach)
#    - Can the same element be part of multiple counted subarrays? (Yes — subarrays can overlap)

### P - Plan
# 2. Write out in plain English what you want to do:
#    Track a running prefix sum as we iterate through the array. At each index, check
#    how many times we've previously seen (prefix_sum - k) — each occurrence means there's
#    a subarray ending here that sums to k. Store each prefix sum in a hash map as we go.

# 3. Translate each sub-problem into pseudocode:
#    - Initialize count = 0, prefix_sum = 0, seen = {0: 1}
#    - For each num in nums:
#        - Add num to prefix_sum
#        - Add seen[prefix_sum - k] to count (0 if not present)
#        - Increment seen[prefix_sum] by 1
#    - Return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def subarray_sum(nums, k):
	count = 0
	prefix_sum = 0
	seen = {0: 1}

	for num in nums:
		prefix_sum += num
		count += seen.get(prefix_sum - k, 0)
		seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

	return count
			

# Example #1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))

# Example #2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2
nums = [1, 2, 3]
k = 3
print(subarray_sum(nums, k))