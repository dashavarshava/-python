""" Lesson 2, task 3.
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""

#решение с list
while True:
    month = int(input())
    if month < 1 or month > 12:
        print("Введите месяц целым числом от 1 до 12")
    else:
        break

#вариант 1
year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if month in year[0:2] or month == year[-1]:
    print("Зима")
elif month in year[2:5]:
    print("Весна")
elif month in year[5:8]:
    print("Лето")
else:
    print("Осень")

#вариант 2
season = ["Зима"] * 2 + ["Весна"] * 3 + ["Лето"] * 3 + ['Осень'] * 3 + ["Зима"]
print(season[month-1])


#решение с dict
my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима" }

while True:
    month = int(input())
    if month < 1 or month > 12:
        print("Введите месяц целым числом от 1 до 12")
    else:
        break

print(my_dict.get(month))