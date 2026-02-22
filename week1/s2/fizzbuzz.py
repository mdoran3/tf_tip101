def fizzbuzz(n):
    num = 1
    while num <= n:
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1

fizzbuzz(13)