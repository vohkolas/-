def n1():
    x = int(input())
    if x % 3 == 0:
        return "Число делится на 3."
    else:
        return "Число не делится на 3."

def n2():
    x = int(input())
    if x.isdigit() == 0:
        return "Введено нечисленное значение."
    elif int(x) == 0:
        return "Деление на 0 выполнить нельзя."
    else:
        return 100 / int(x)

def n3():
    x = input()
    sp = x.split(".")
    if int(sp[0]) * int(sp[1]) == int(sp[-1]) % 100:
        return True
    else:
        return False

def n4():
    x = input()
    k1 = 0
    k2 = 0
    if len(x) % 2 != 0:
        return 0

    for i in range(len(x) // 2):
        print(i)
        k1 = k1 + int(x[i])
        k2 = k2 + int(x[-i - 1])
    print(k1, k2)
    if k1 == k2:
        return "Счастливый билет"
    else:
        return "Не счастливый билет"
print(n4())