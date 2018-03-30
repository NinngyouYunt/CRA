def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(10)
print(f(1))
print(f(1))