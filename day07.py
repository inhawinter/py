def a():  # generator
    yield 1
    yield -9
    yield 3


def b():  # normal function
    return 1  # stop
    return -9
    return 3

print(type(a()), b())
c = a()
print(c)

for i in c:
    print(i)

for i in c:
    print(i)