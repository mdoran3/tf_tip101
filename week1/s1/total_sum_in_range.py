def sum_range(start, stop):
    sum = 0
    for i in range(start, stop+1):
        sum += i
    return sum

print(sum_range(3, 9))