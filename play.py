import itertools  

a = [1, 2, 3]
b = [4, 5, 6]
c = itertools.product(range(1, 5), range(2, 8))


def fn(x, y):
    print(x, y)

count = list(1 for i, k in itertools.product(range(-1, 2), range(1, 2)))

print(count)
