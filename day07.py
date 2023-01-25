def document_info(func):  # decorator
    def new_function(*args, **kwargs):
        print('실행 중인 함수:', func.__name__)
        print('위치 인수들', args)
        print('키워드 인수들', kwargs)
        result = func(*args, **kwargs)
        print('실행결과:', result)
        return result
    return new_function


@document_info
def squares(n):
    return n * n


@document_info
def subtract(a, b):
    return a - b


print(squares(5))
print(subtract(5, 99))

