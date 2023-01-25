# prime number v1.1
# function

def isprime(n):
    """
    매개변수로 받은 정수가 소수인지 판정하는 함수
    :param n: integer number
    :return: True or False
    """
    if n <= 1:
        return False

    for k in range(2, n):
        if n % k == 0:
            return False

    return True


number_list = input('input 2 integer number : ').split()
start = int(number_list[0])
end = int(number_list[1])

if end < start:
    start, end = end, start

for number in range(start, end+1):
    if isprime(number):
        print(number, end=' ')
