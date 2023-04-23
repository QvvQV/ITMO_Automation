def task_1() -> None:
    #назначение переменных
    a: int = 1
    b: float = 1.1
    c: str = 'stroka'
    d: list = [1, 2]
    e: bool = (a>b)
    return (a, type(a)), (b, type(b)), (c,type(c)), (d, type(d)), (e, type(e))
# вызов и вывод функции
print(task_1())




def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    return 'a[0:3] = ', a[0:3]

print(task_2()) #Может это срез для списка



def task_3() -> int:
    a = int(input('введите число '))
    return a ** 2
print(task_3())
