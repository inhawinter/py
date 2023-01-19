import copy

odds = list(range(1, 11, 2))
print(odds)

# mixed = [3, 4, 1, 7, 'A', '한', '김', 5, 'b', 'B']
# TypeError: '<' not supported between instances of 'str' and 'int'

mixed = ['3', '4', '1', '7', 'A', '한', '김', '5', 'b', 'B']
# ascending : arabic number, alphabet UpperCase, alphabet LowerCase, Korean
mixed.sort(reverse=True)  # descending
#print(mixed)

# copy
# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
#
# a[1] = 'inha'
# c[2] = 'univ'
# print(a, b, c, d)


# a = [1, [9, -7], 3]
# b = a.copy()
# c = list(a)
# d = a[:]
#
# a[1][1] = 'inha'
# #a[1][0] = -99
# print(a, b, c, d)

a = [1, [9, -7], 3]
b = copy.deepcopy(a)

a[1][1] = 'inha'
#a[1][0] = -99
print(a, b)