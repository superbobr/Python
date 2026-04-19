"""Write a generator function gen_fibonacci() that infinitely yields Fibonacci numbers (0, 1, 1, 2, 3, 5, 8, ...).
In the main code, print the first 10 numbers using a for loop and break."""

def gen_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for i, num in enumerate(gen_fibonacci()):
    print(num)
    if i == 9:
        break