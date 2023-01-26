# prime number v1.4
# exception
import tkinter as tk
from tkinter import messagebox


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
    try:
        start = int(en_start.get())
        end = int(en_end.get())

        if end < start:
            start, end = end, start

        results = ''
        for number in range(start, end + 1):
            if isprime(number):
                #results = results + str(number) + ' '
                results = results + f'{number} '
    except ValueError as err:
        messagebox.showerror('에러정보', f'숫자를 입력해주세요\n{err}')
    except Exception as other:
        lbl_result.config(text=f'예외 발생 : {other}')
    else:
        lbl_result.config(text=results)
    finally:
        pass


win = tk.Tk()
win.title('구간 소수 계산 프로그램')
win.geometry('300x100')

lbl_result = tk.Label(win, text='아래 두 정수를 입력하세요')
en_start = tk.Entry(win)
en_end = tk.Entry(win)
btn_prime = tk.Button(win, text='소수 계산', command=click_prime)

lbl_result.pack()
en_start.pack()
en_end.pack()
btn_prime.pack(fill='x')

win.mainloop()
