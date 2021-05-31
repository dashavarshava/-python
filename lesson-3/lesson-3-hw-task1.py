""" Lesson 3, task 1.
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку
ситуации деления на ноль.
"""


def division():
    try:
        a = float(input("Первое число: "))
        b = float(input("Второе число: "))
        c = a / b
    except ZeroDivisionError:
        return
    return c


print(division())
