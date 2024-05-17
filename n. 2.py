def n1():
    x1 = input("Введите пароль: ")
    x2 = input("Подтвердите пароль: ")
    if x1 == x2:
        print("Пароль принят.")
    else:
        print("Пароль не принят.")

def n2():
    x = int(input("Номер места: "))
    if x % 2 == 0:
        print("Верхнее место.")
    else:
        print("Нижнее место.")
def n3():
    x = int(input())
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        print("Год ", x, "– високосный.")
    else:
        print("Этот год не високосный.")
def n4():
    x = []
    for i in range(2):
        a = input()
        x.append(a)
    # print(x)
    if "Красный" in x and "Синий" in x:
        print("Фиолетовый")
    elif "Желтый" in x and "Синий" in x:
        print("Зеленый")
    elif "Желтый" in x and "Красный" in x:
        print("Оранжевый")
    elif x[0] == x[1] and x[0] == "Красный" or x[0] == "Синий" or x[0] == "Желтый":
        print(x[0])
    else:
        print("Ошибка")

print(n1())