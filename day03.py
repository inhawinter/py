# prime number v0.3

number = int(input('input integer number : '))
is_prime = True  # True가 유지 되면 소수

for k in range(1, number+1):  # 2부터 입력 된 수 앞까지 반복
    if number % k == 0:  # k로 나누어 떨어지면
        # counts = counts + 1
        is_prime = False

#if is_prime == True:  # is_prime 변수의 True 값이 유지되면 소수
if is_prime:  # is_prime 변수의 True 값이 유지되면 소수
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')
