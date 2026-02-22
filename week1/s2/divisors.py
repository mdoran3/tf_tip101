def find_divisors(n):
    div = 1
    divs = []
    while div <= n:
        if n % div == 0:
            divs.append(div)
        div += 1
    return divs

lst = find_divisors(6)
print(lst)