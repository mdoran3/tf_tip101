#########################
# PROBLEM 2: HOW MANY 1s
#########################

# Given a sorted list of integers containing only 0s and 1s,
# count the total number of 1’s in the array in O(log n) time.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#   Can the list be empty, and if so should we return 0?
#   Are the 0s always guaranteed to come before all the 1s?

### P - Plan
# 2. Write out in plain English what you want to do:
#   Since the list is sorted, all 0s come first and all 1s come last.
#   Use binary search to find the index of the first 1 in the list.
#   If the middle element is a 1, record that index and search left for an earlier 1.
#   If the middle element is a 0, discard the left half and search right.
#   Once the first 1 is found, subtract its index from the total length to get the count of 1s.

# 3. Translate each sub-problem into pseudocode:
#   set lo = 0, hi = len(lst) - 1, first_one = len(lst)
#   while lo <= hi:
#       mid = (lo + hi) // 2
#       if lst[mid] == 1:
#           first_one = mid
#           hi = mid - 1
#       else:
#           lo = mid + 1
#   return len(lst) - first_one

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_ones(lst):
    lo, hi = 0, len(lst) - 1
    first_one = len(lst)  # default: no 1s found
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == 1:
            first_one = mid
            hi = mid - 1  # keep searching left for earlier 1
        else:
            lo = mid + 1
    return len(lst) - first_one
			
test_lst = [0, 0, 0, 0, 1, 1, 1]
print(count_ones(test_lst))
test_lst2 = [0, 0, 0, 0, 1, 1, 1, 1, 1]
print(count_ones(test_lst2))
test_lst3 = [0, 0, 0, 1, 1, 1, 1, 1, 1]
print(count_ones(test_lst3))