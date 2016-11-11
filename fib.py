first = 0
second = 1

n = int(input('Enter n value: '))
for i in range(0, n):
    if i <= 1:
        new = i
    else:
        new = first + second
        first = second
        second = new

    print(new)

