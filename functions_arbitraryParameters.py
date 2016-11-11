def arithmetic_mean(*values):
    if len(values) == 0:
        print('Values can\'t be empty')
    else:
        return sum(values) / len(values)

print(arithmetic_mean(45, 32, 89, 78))
print(arithmetic_mean())

