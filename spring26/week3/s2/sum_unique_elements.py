# Write a function sum_of_unique_elements() that takes in two 
# lists of integers, lst1 and lst2, as parameters and returns 
# the sum of the elements that are unique in lst1.

# An element is unique if:

# it appears exactly once in lst1
# it does not appear in lst2

def sum_of_unique_elements(lst1, lst2):
	uniques = dict()
	for num in lst1:
		if num not in lst2 and num not in uniques:
			uniques[num] = 1
		elif num not in lst2 and num in uniques:
			uniques[num] += 1
	sum = 0
	for num_u in uniques:
		if uniques[num_u] == 1:
			sum += num_u
	return sum

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)