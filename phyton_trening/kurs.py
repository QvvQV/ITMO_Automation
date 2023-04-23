#a: list[1, 2, 3, 4] - бакалавр
#b: list[5, 6] - магистр
#c: list[7, 8, 9] - аспирант

a = 3
def kurs_1(a):
    if a == 1 or a == 2 or a == 3 or a == 4:
        print('Бакалавр')
    elif a == 5 or a == 6:
        print('Магистр')
    elif a == 7 or a == 8 or a == 9:
        print('Аспирант')
    else:
        print('Введите корректный курс')
kurs_1(a)