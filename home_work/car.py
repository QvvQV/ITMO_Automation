#4.	В отдельном файле напишите программу с классом Car.
#a.	Создайте конструктор класса Car. Создайте атрибуты класса
# Car — color (цвет), type (тип), year (год).
#b.	Напишите пять методов.
#i.	Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
#ii.	Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
#iii.	Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
#iv.	Пятый — присвоение автомобилю цвета

class Car:

    def __init__(self, color, type, year, a):
        self.color = color
        self.type = type
        self.year = year
        self.a = a

    def pusk(self):
        if self.a > 0:
            return 'Автомобиль заведён'
        elif self.a <= 0:
            return('Автомобиль заглушен')

pusk1 = Car ('black', 'Mazda', '1980', 0)
pusk2 = Car ('red', 'Honda', '2000', 1)
print('цвет: ' + pusk1.color + "\n" + 'тип: ' + pusk1.type + '\n' + 'год: ' + pusk1.year + '\n ' + pusk1.pusk())

print('\n')

print('цвет: ' + pusk2.color + "\n" + 'тип: ' + pusk2.type + '\n' + 'год: ' + pusk2.year + '\n ' + pusk2.pusk())
