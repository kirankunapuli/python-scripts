n = 2
while n <= 20:
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', int(n / x))
            break
        else:
            print(n, 'is a prime number')
        n += 1
