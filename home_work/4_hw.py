# 1.	создайте класс прямоугольника.
# a.	атрибуты - прямоугольнику можно задать ширину и высоту
# b.	методы - реализуйте 2 метода:
# i.	расчет площади прямоугольника
# ii.	расчет периметра прямоугольника
# c.	создайте 3 объекта, рассчитайте площадь и периметр для каждого.
# Результаты выводить в консоль


class Rectangle:

    def __init__(self, hight, widht):

            self.hight = hight
            self.widht = widht

#Расчёт периметра прямоугольника

    def per(self):
        if self.hight > 0 and self.widht > 0:
            return (self.hight * self.widht)*2
        else:
            print('Введены неверные данные')

# Расчёт площади прямоугольника

    def area(self):
        if self.hight > 0 and self.widht > 0:
            return (self.hight * self.widht)
        else:
            print('Введены неверные данные')

Rec1 = Rectangle (3, 5)
Rec2 = Rectangle (-3, 5)
Rec3 = Rectangle (3, 15)
print('Периметр прямоугольника равен ', Rec1.per(), ',', Rec2.per(), ',', Rec3.per())
print('Площадь прямоугольника равна ', Rec1.area(), ',', Rec2.area(), ',', Rec3.area())

# 2.	Создайте класс Math.
# a.	Создайте два атрибута — a и b.
# b.	Напишите методы
# i.	addition — сложение,
# ii.	multiplication — умножение,
# iii.	division — деление,
# iv.	subtraction — вычитание.
#
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия
# и печатать ответ

print('\n')


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_1(self):
        print('сложение: ',self.a + self.b)

    def multi_2(self):
        print('умножение: ', self.a * self.b)

    def div_3(self):
        print('деление: ', self.a/self.b)

    def subt_4(self):
        print('вычитание: ', self.a - self.b)

M1 = Math (5, 7)
M2 = Math (-5, 3)

M1.add_1()
M1.multi_2()
M1.div_3()
M1.subt_4()

M2.add_1()
M2.multi_2()
M2.div_3()
M2.subt_4()

print('\n')
# 3.	откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
#
# a.	Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
#
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# -	текст кнопки (пример: “Text Box”)
# -	тип - одинаковый для всех “Кнопка”
# -	локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст
# “Клик по кнопке { ТЕКСТ КНОПКИ }”
#
# b.	выведите текст для каждой кнопки
# c.	вызовите “Клик” для каждой кнопки

#import webbrowser
#webbrowser.open_new_tab('https://demoqa.com/text-box')

class Button:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return 'Клик по кнопке -{}'.format(self.text)

box = Button('Text Box', 'https://demoqa.com/text-box', 'loc')
check = Button('Check Box', 'https://demoqa.com/checkbox', 'loc')
radio = Button('Radio Button', 'https://demoqa.com/radio-button', 'loc')
web = Button('Web Tables', 'https://demoqa.com/webtables', 'loc')
Buttons = Button('Buttons', 'https://demoqa.com/buttons', 'loc')
Links = Button('Links', 'https://demoqa.com/links', 'loc')
Broken = Button('Broken Links - Images', 'https://demoqa.com/broken', 'loc')
Up = Button('Upload and Download', 'https://demoqa.com/upload-download', 'loc')
Dyn = Button('Dynamic Properties', 'https://demoqa.com/dynamic-properties', 'loc')


print(box.text, box.link, box.click())
print(check.text, check.link, check.click())
print(radio.text, radio.link, radio.click())
print(web.text, web.link, web.click())
print(Buttons.text,Buttons.link,Buttons.click())
print(Links.text, Links.link, Links.click())
print(Broken.text, Broken.link, Broken.click())
print(Up.text, Up.link, Up.click())
print(Dyn.text, Dyn.link, Dyn.click())
#print('Кнопка' + box.text + 'имеет ссылку' + box.link + 'локатор' + box.loc)

