def test(start=0, end=5):
    n = start
    #for i in range(start, end+1):
    while n <= end:
        yield n
        n = n + 1

print(test)
g = test(5, 10)
# g = test()
print(g)
for k in g:
    print(k)

for k in g:
    print(k)

#a = (p for p in zip([1, 2, 3],[4, 5 ,6],[7, 8, 9, 10]))
a = (p for p in zip({(1, 1): 3.99, (1, 2): 4.31}, {(2, 1): 4.19, (2, 2): 4.01}))
print(type(a), a)
for i in a:
    print(i)
