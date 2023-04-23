# Функция на вход получает два произвольных числа.
# Вывести в консоль наибольшее из чисел.

a = 145
b = 0

def hw_3(a, b):
    if a > b:
        print(a)
    else:
        print(b)
hw_3(a, b)

# Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”


if (a - b) >= 135:
    print('Да')
else:
    print('Нет')

# Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)
s = 5
if s == 1 or s == 2 or s == 12:
    print('Winter')
elif s == 3 or s == 4 or s == 5:
    print("Spring")
elif s == 6 or s == 7 or s == 8:
    print('Summer')
elif s == 9 or s == 10 or s == 11:
    print('Autumn')
else:
    print('Введите корректное число')

# Другой вариант решения

seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = 8
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

#	Функция на вход получает три произвольных числа.
#   Если все числа больше 10, то вывести на экран “yes”, иначе “no”


z = 15
y = 15
x = 7

if z > 10 and x > 10 and y > 10:
    print('da')
else:
    print('net')

# Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.

list1 = [-1, -3, -4, -5, -7]

pos_count, neg_count = 0, 0

for num in list1:
    if num >= 0:
        pos_count += 1
    else:
        neg_count += 1

print('Позитивное количество чисел в списке', pos_count)

# Функция на вход получает 2 переменные.
# a.Кол-во лет (int)
# b.Кол-во месяцев (int)
# Вывести в консоль количество дней за это время.
# Считать, что в каждом месяце 29 дней.

year = 15
month = 7

print('Количество дней = ' +str(month*29+year*365))
