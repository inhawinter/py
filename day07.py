# Lambda function (after)

import random


def process(no_lists, f):
    """
    리스트와 함수를 받아 리스트의 원소들을 받은 함수에 모두 적용
    :param no_lists: 리스트
    :param f: 함수
    :return: void
    """
    for no in no_lists:
        print(f(no))


numbers = [random.randint(1, 10) for i in range(5)]
print(numbers)
process(numbers, lambda x: x * x)  # squares
process(numbers, lambda x: x + x)  # doubles
