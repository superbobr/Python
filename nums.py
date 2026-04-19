"""Write a program that:

Creates a list nums = [1, 2, 3, 4, 5, 6, 7, 8].
Constructs a generator expression that yields every second element, starting from the first (index 0): 1, 3, 5, 7, …
Prints the first 4 values from this generator, one per line."""

nums = [x for x in range(1, 9)]

result = (i for i in nums[::2])

for num in range(4):
    print(next(result))