# Урок 1
# Задание 1
a = int(123)
b = 'Привет'
print(a, b)
c = int(input('Введите число:'))
print('Ваше число + 123 =', c + a)

# Задание 2
sek = int(input('Введите время в секундах:'))
hour = sek // 3600
minute = (sek - hour * 3600) // 60
second = sek - hour * 3600 - minute * 60
print(hour, ':', minute, ':', second, sep = '')

# Задание 3
n = int(input('Введите число:'))
nstr = str(n)
nn = nstr + nstr
nnn = nstr + nstr + nstr
print(n + int(nn) + int(nnn))

# Задание 4
num = int(input('Введите число:'))
num2 = num % 10
num = num//10
while num > 0:
    if num % 10 > num2:
        num2 = num % 10
    num = num//10
print('Самая большая цифра числа:', num2)

# Задание 5
revenue = int(input('Введите выручку компании:'))
expend = int(input('Введите издержки компании:'))
if revenue >= expend:
    print('Вы отработали в плюс')
else:
    print('Вы отработали в минус')
profit = revenue - expend
if profit >= 0:
    print('Выручка составила:', profit)
employee = int(input('Введите число сотрудников:'))
print('Прибыль на одного сотрудника', int(profit / employee))

# Задание 6
x = int(input('Сколько пробегает спортсмен сейчас:'))
y = int(input('Сколько должен пробежать:'))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print('Через', day, 'дней спортсмен достигнет результата')

#Спасибо)