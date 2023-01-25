def document_info(func):  # decorator
    def new_function(*args, **kwargs):
        print('실행 중인 함수:', func.__name__)
        print('위치 인수들', args)
        print('키워드 인수들', kwargs)
        result = func(*args, **kwargs)
        print('실행결과:', result)
        return result
    return new_function


def squares(n):
    return n * n


def subtract(a, b):
    return a - b


info_squares = document_info(squares)
r1 = info_squares(9)
print(r1)
# print(squares(7))
print('==================')
info_minus = document_info(subtract)
r2 = info_minus(99, 7)
print(r2)