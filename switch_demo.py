# A dictionary based switch statement

# Use has-key

choice = 'ham'
print({'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}[choice])

if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')
