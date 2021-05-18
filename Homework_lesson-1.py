#Task 1
#hello_world
a = 'hello_world'
print(a)

#hello_world 12
b = 12
print(a,b)

#1980 1980 1980
c = 1980
a = b = c
print(a, b, c)

#Вывод вводимой строки на экран
name = input()
print(name)

#Вывод целочисленного числа от пользователя на экран
age = int(input())
print(age, type(age))
print("My name is ", name," and I'm ", age)

#Вывод числа c плавающей точкой на экран от пользователя
fraction = float(input())
print(fraction, type(fraction))

#Преобразование в целочисленное число и вывод на экран
unit = int(float(input()))
print(unit, type(unit))


def check_time():
    """Task 2"""
    time = int(input())
    hour = (time//3600)
    minute = (time%3600//60)
    second = (time-hour*3600-minute*60)
    print("{0:0>2}:{1:0>2}:{2:0>2}".format(hour,minute,second))


check_time()


def find_sum():
    """Task 3"""
    n = str(input())
    nn = int(n+n)
    nnn = int(n+n+n)
    n = int(str(n))
    nsum = n+nn+nnn
    print(n," + ",nn," + ",nnn," = ",nsum)


find_sum()


def find_max():
    """Task 4"""
    numbers = [int(i) for i in input()]
    max_number = numbers[0]
    i = 1

    while i < len(numbers):
        if numbers[i] > max_number:
            max_number = numbers[i]
        i = i+1

    print(max_number)


find_max()


def count_profit():
    """Task 5"""
    gain = abs(float(input("Введите выручку компании ")))
    costs = abs(float(input("Введите издержки компании ")))

    if gain > costs:
        profit = gain - costs
        print("Ваша прибыль = ", profit)
        per_employee = int(input("Введите количество сотрудников "))
        if per_employee != 0:
            calc_per_employee = profit/per_employee
            print("Прибыль на сотрудника: ", calc_per_employee)
        else:
            print(profit, "Внимание! Нет сотрудников")
    else:
        print("Вы в убытке!")


count_profit()


def count_km():
    """Task 6"""
    a = float(input("Введите расстояние в первый день пробежки "))
    b = float(input("Введите ожидаемое расстояние пробежки "))
    i = 1

    while a < b:
        a = a*1.1
        i = i+1

    print("На ", i, "-й день спортсмен достигнет результата — не менее ", b, "км")


count_km()