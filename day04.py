# dictionary comprehension

# univ = 'inha university'
# letter_counts = {letter: univ.count(letter) for letter in univ}
# print(letter_counts)

univ = 'inha university'
letter_counts = dict()
for letter in univ:
    letter_counts[letter] = univ.count(letter)
print(letter_counts)


#prime_set = set([2, 3, 5, 7, 11, 7, 3])
prime_set = set((2, 3, 5, 7, 11, 7, 3, 19, 19))
print(prime_set)
prime_set.add(13)
prime_set.remove(3)
print(prime_set)