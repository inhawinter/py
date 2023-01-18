# 새로운 gmail 계정 준비
# git, github

import copy
a = ['김지혜', '곽다인', '김설화', '이영철', '조희령']
b = copy.deepcopy(a)
print(b, a)
a[0] = '김인하'
print(b, a)
print(id(a), id(b))


# a = ['김지혜', '곽다인', '김설화', '이영철', '조희령']
# b = a
# print(b, a)
# a[0] = '김인하'
# print(b)
# print(id(a), id(b))

# x = 99
# y = x + 5
# print(y)

# literal
# 77 = 99
# 'univ' = 'inha'

# type
# print(type(2.7e-1))

# countdown_list = [5, 4, 3, 2, 1, "hey!"]
# countdown_list[2] = -99
# for countdown in countdown_list:
#     print(countdown)

# countdown_tuple = (5, 4, 3, 2, 1, "hey!")
# # countdown_tuple[2] = -99  # TypeError: 'tuple' object does not support item assignment, tuple is immutable
# temp = list(countdown_tuple)
# temp[2] = -99  # mutable
# countdown_tuple = tuple(temp)
# print(countdown_tuple[2])  # 3 -> -99
#
# for countdown in countdown_tuple:
#     print(countdown)


# 화씨 섭씨 온도 변환 프로그램
# (100°F − 32) × 5/9 = 37.778°C

# fahrenheit = float(input("Fahrenheit : "))
# celsius = (fahrenheit - 32.0) * (5.0/9.0)
# print('화씨 온도', fahrenheit, '도는 섭씨 온도', celsius, '도 입니다')  # comma
# print('화씨 온도 %.3f도는 섭씨 온도 %.3f도 입니다' % (fahrenheit, celsius))  # old style, c language like
# print('화씨 온도 {1:.3f}도는 섭씨 온도 {0:.3f}도 입니다'.format(fahrenheit, celsius))  # modern style, format()
# print(f'화씨 온도 {fahrenheit:.3f}도는 섭씨 온도 {celsius:.3f}도 입니다')  # newest style, f-string



