"""
Problem 2:

Write a program that finds the most optimized set of 6 units to shop with for values
fewer than 100. Example: Units used are 1, 2, 5, 10, 20, 50 1: 1 (1 unit used) 2: 2 (1
unit used) 3: 1+2 (2 units used) 4: 2+2 (2 units used) ... 98: 1+2+5+20+20+50 (6 units
used) 99: 2+2+5+20+20+50 (6 units used) AVG of units = 16.5

"""

# Solution:

from itertools import combinations_with_replacement

def find_optimized_set(target_value, units):
    min_units = float('inf')
    optimized_set = None

    for combo in combinations_with_replacement(units, 6):
        if sum(combo) == target_value:
            if len(combo) < min_units:
                min_units = len(combo)
                optimized_set = combo

    return optimized_set, min_units

target_value = int(input("Enter the target_value: "))
units = [1, 2, 5, 10, 20, 50]

optimized_set, min_units = find_optimized_set(target_value, units)

if optimized_set:
    print(f"The most optimized set of 6 units to shop with for {target_value} is: {optimized_set} using {min_units} units.")
    print(f"Average units used: {sum(optimized_set)/6}")
else:
    print("No optimized set found for the target value.")
    
# Output:

"""
Enter the target_value: 99
The most optimized set of 6 units to shop with for 99 is: (2, 2, 5, 20, 20, 50) using 6 units.
Average units used: 16.5

"""