# Урок 3
# Задание 1: Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

num1, num2 = int(input()), int(input())
if num2 == 0:
    print('На нуль делить нельзя')
else:
    print(num1 / num2)

# Задние 2: Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name = input('Введите Ваше имя: ')
surnames = input('Введите вашу фамилию: ')
year = input('Введите Ваш год рождения: ')
city = input('Введите Ваш город проживания: ')
email = input('ведите Вашу почту: ')
telephone = input('Введите Ваш номер телефона: ')
print(name, surnames, year, city, email, telephone)

# Задание 3: Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

# Задание 4: Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

a = int(input())
n = int(input())
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

# Задание 5 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

summa = 0
num = input("Введите числа через пробел: ").split()
is_exit = False
while True:
    for item in num:
        if item == "q":
            is_exit = True
            break
        if not item.isdigit()
            print(f"Это не число {item}")
            break
        summa += int(item)
    print(f"Сумма: {summa}")
    if is_exit:
        break
    num = input("Введите числа через пробел: ").split()

# Задание 6 Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def capitalize(text): return text.title()
print(capitalize(input()))