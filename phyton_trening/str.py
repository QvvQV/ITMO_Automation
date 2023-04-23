str_1 = 'test'
str_2 = 'test1'

def str(str_1, str_2):
    if str_1 in str_2:
        print('Da')
    else:
        print('Net')
str('test', 'test2')

a = 50

if a > 100 or a < -100:
    print('-')
else:
    print('+')