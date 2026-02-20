def sum_positive_range(stop):
    sum = 0
    for i in range(stop+1):
        sum += i
    return sum

print(sum_positive_range(6))