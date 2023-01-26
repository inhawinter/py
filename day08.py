# exception
try:
    # raise Exception("예외처리 복습")
    # print(5+'8')
    raise TypeError("타입 에러")
    expr = input('분자 분모 입력 (띄어쓰기로 구분): ').split()
    print(int(expr[0]) / int(expr[1]))
except ValueError as err:
    print(f'숫자를 입력해주세요 ({err})')
except IndexError as err:
    print(f'입력 값의 범위에 문제가 있습니다 ({err})')
except ZeroDivisionError as err:
    print(f'분모에 0이 올 수 없습니다 ({err})')
except Exception as other:
    print(f'예외가 발생했습니다 ({other})')
else:  # 예외가 발생하지 않았을 때 동작
    print('프로그램 정상', end=' ')
finally:  # 예외 발생 여부와 상관 없이 항상 실행
    print('종료')
