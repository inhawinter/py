def a():
    def b():
        return "안쪽 함수 실행"
    return b

print(a())
c = a()
print(c())
# print(b())  # a함수에서만 볼 수 있다.

