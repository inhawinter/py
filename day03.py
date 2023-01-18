# prime number v0.1

number = int(input('input integer number : '))
counts = 0

for k in range(1, number+1):  # 1부터 입력 된 수까지 반복
    if number % k == 0:  # k로 나누어 떨어지면
        counts = counts + 1

if counts == 2:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')
