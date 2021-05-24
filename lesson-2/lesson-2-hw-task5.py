""" Lesson 2, task 5.
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
new = int(input())

#вариант 1
my_list.append(el)
my_list.sort(reverse=True)
print(my_list)

#вариант 2
if my_list[-1] >= new:
    my_list.append(new)
else:
    for ind, el in enumerate(my_list):
        if el < new:
            my_list.insert(ind, new)
            break

print(my_list)
