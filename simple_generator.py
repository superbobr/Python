"""Write a generator function `even_numbers(n)` that yields all even numbers from 0 to `n` (inclusive, if `n` is even).
 Test its functionality by printing all generated values in a `for` loop."""

def even_numbers(n):
    num = 0
    while num <= n:
        yield num
        num += 2

for num in even_numbers(5):
    print(num)