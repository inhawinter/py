# prime number v0.8

number_list = input('input 2 integer number : ').split()
start = int(number_list[0])
end = int(number_list[1])

for number in range(start, end+1):
    if number > 1:
        for k in range(2, number):
            if number % k == 0:
                break
        else:
            print(number, end=' ')
