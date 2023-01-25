# Closures
def calculate():
    x = 5
    y = 10

    def add_sub(n):  # inner function act as closure
        return x + n - y

    return add_sub


calc = calculate()
print(type(calc), calc)
print(calc(3))
for i in range(10, 15):
    print(calc(i))
