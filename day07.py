def calculate_fee(*ages):  # 가변 매개변수 (튜플로 받는다)
    total = 0
    for age in ages:
        if 19 <= age:  # adult
            total = total + 10000
        else:  # kids
            total = total + 4000
    return total


print(calculate_fee(21, 25, 20))
print(calculate_fee(7, 45, 43, 10))
