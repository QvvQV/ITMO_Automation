a = 145
b = 0

def hw_3(a, b):
    if a > b:
        print(a)
    else:
        print(b)
hw_3(a, b)


if (a - b) >= 135:
    print('Да')
else:
    print('Нет')

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

z = 15
y = 15
x = 7

if z > 10 and x > 10 and y > 10:
    print('da')
else:
    print('net')