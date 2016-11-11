keys = ['spam', 'ham', 'eggs', 'bacon']
values = [1.25, 1.99, 0.99, 1.10]

food = dict(zip(keys,values))

# food = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}

choice = str(input('Enter a key: '))
if choice in keys:
    print(choice, '--', food[choice])
else:
    print("Bad choice")
