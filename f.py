def fib1(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return fib1(n-1) + fib1(n-2)

print(fib1(10))
