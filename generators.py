"""Write a program that implements and uses multiple generators.

Implement a generator function:
gen_range(start, end) — yields integers sequentially from start to end - 1 (a half-open range).

Implement a generator function:
gen_symbols() — yields characters sequentially from the list ['@', '#', '%'].

Implement a function:
chain() — merges streams of values: first performs yield from gen_range(1, 4), then yield from gen_symbols().

In the main part of the program, iterate through the values yielded by chain(), and print each value on a separate line."""

def gen_range(start, end):
    num = start
    while num < end:
        yield num
        num += 1

def gen_symbols():
    symbols = ['@', '#', '%']
    for symbol in symbols:
        yield symbol

def chain():
    yield from gen_range(1, 4)
    yield from gen_symbols()

for value in chain():
    print(value)

