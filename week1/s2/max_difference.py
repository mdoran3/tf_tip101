def max_difference(lst):
    max_num = float('-inf')
    min_num = float('inf')
    for num in lst:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num - min_num

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)