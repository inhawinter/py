# prime number v0.9

number_list = input('input 2 integer number : ').split()
start = int(number_list[0])
end = int(number_list[1])

if end < start:
    start, end = end, start  # tuple packing & unpacking

for number in range(start, end+1):
    if number > 1:
        for k in range(2, number):
            if number % k == 0:
                break
        else:
            print(number, end=' ')
