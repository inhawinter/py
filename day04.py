import random

# hard coding
# numbers = list()
# numbers.append(random.randint(1, 100))
# numbers.append(random.randint(1, 100))
# numbers.append(random.randint(1, 100))
# numbers.append(random.randint(1, 100))
# numbers.append(random.randint(1, 100))
# print(numbers)

# for loop
# numbers = []
# for k in range(5):
#     numbers.append(random.randint(1, 100))
# print(numbers)

# list comprehension
# numbers = [random.randint(1, 100) for k in range(5)]
# print(numbers)


# for loop
# odds = []
# for k in range(1, 11):
#     if k % 2:
#         odds.append(k)
# print(odds)


# list comprehension
odds = [k for k in range(1, 11) if k % 2]
print(odds)

# index
# for i in range(len(odds)):
#     odds[i] = str(odds[i])
# print(odds)
# print('/'.join(odds))  # 리스트의 원소들을 하나의 문자열로 만들어준다


# list
# temp = list()
# for odd in odds:
#     temp.append(str(odd))
# print(temp)
# print('/'.join(temp))  # 리스트의 원소들을 하나의 문자열로 만들어준다


# enumerate
for item in enumerate(odds):  # (index, value) 튜플 형태로 리턴
    # print(item)
    odds[item[0]] = str(item[1])
print(odds)
print('/'.join(odds))  # 리스트의 원소들을 하나의 문자열로 만들어준다







