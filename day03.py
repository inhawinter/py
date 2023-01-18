# prime number v0.5

number = int(input('input integer number : '))
is_prime = True

if number <= 1:
    is_prime = False
else:
    for k in range(2, number):
        if number % k == 0:
            is_prime = False
            break

if is_prime:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')
