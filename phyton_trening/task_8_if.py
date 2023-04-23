# программа проверяет является число положительным
# или отрицательным и выводит соответсвующее сообщение

num = 3

# Также попробуйте следующее значение num.
# num = - 5
# num = 0

if num >=0:
    print('Число больше или равно 0')
else:
    print('Число отрицательное')

num_float = 3.4

# Также попробуйте следующее значение num_float.
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print("Ноль")
else:
    print('Число отрицательное')

permit_print = True

if num > 0 and permit_print:
    print('num положительное число')
elif not permit_print:
    print('Печать запрещена')