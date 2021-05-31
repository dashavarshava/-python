""" Lesson 3, task 3.
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(var1, var2, var3):
    iter_obj = (var1, var2, var3)
    return sum(iter_obj) - min(iter_obj)


res = my_func(int(input("Число 1: ")), int(input("Число 2: ")), int(input("Число 3: ")))
print(res)
