import random


def calculate_fee(ages):  # 리스트
    total = 0
    adults = 0
    kids = 0
    for age in ages:
        if 19 <= age:  # adult
            total = total + 10000
            adults += 1
        else:  # kids
            total = total + 4000
            kids += 1
    return [len(ages), adults, kids, total]


# results = calculate_fee([7, 45, 43, 10])
no_of_visitor = int(input(f'몇 분 이세요? '))
ages = [random.randint(1, 100) for age in range(no_of_visitor)]
print(ages)
results = calculate_fee(ages)
print(f'{results[0]}명 방문 하셨고 어른 {results[1]}명, 어린이 {results[2]}명 총 요금은 {results[-1]}원 입니다')

# 4명 방문 하셨고 어른 2명, 어린이 2명 총 요금은 28000원 입니다
