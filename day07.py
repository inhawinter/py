# prime number v1.3
# gui (button 1, entry 2, label 1)
import tkinter as tk


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


def click_prime():
    start = int(en_start.get())
    end = int(en_end.get())

    if end < start:
        start, end = end, start

    results = ''
    for number in range(start, end + 1):
        if isprime(number):
            #results = results + str(number) + ' '
            results = results + f'{number} '

    lbl_result.config(text=results)


win = tk.Tk()
win.title('구간 소수 계산 프로그램')
win.geometry('300x150')

lbl_result = tk.Label(win, text='아래 두 정수를 입력하세요')
en_start = tk.Entry(win)
en_end = tk.Entry(win)
btn_prime = tk.Button(win, text='소수 계산', command=click_prime)

lbl_result.pack()
en_start.pack()
en_end.pack()
btn_prime.pack(fill='x')

win.mainloop()
