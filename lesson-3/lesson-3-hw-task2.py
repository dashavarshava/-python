""" Lesson 3, task 2.
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""


def user_data(name, lastname, dob, city, email, phone):
    print(f"{name} {lastname} {dob} {city} {email} {phone}")


user_data(lastname=str(input("Фамилия: ")), name=str(input("Имя: ")), phone=str(input("Телефон: ")), dob=str(input("Год рождения: ")),
          city=str(input("Город проживания: ")), email=str(input("Email: ")))
