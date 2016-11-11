import sys
import copy

print(sys.version)

c=[1,2,3,4,5,6]


x = copy.copy(c)
y = copy.deepcopy(c)

print(y)
