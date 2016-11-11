import sys
import numpy as np

welcomeString = input('Enter one of the following\n Mean, Median, Mode, Range\n')
welcomeString = welcomeString.lower()

numbers = input("Enter numbers to calculate: ")
numbers = list(map(float, numbers.split(' ')))

average_function = {"mean": np.average,
                    "median": np.median,
                    # "mode": np.mode,
                    "range": np.arange,
                    }

try:
    print(average_function[welcomeString](numbers))
except KeyError:
    sys.exit("You entered invalid average type!")

# input()
