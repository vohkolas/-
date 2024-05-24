def n1():
    a = [5, 3, 0, 1, 9]
    x = int(input())
    if x in a:
        print("+")
    else:
        print("-")

def n2():
    a = [1, 2, 3, 2, 4, 5, 5, 6]
    b = []
    dubl = []
    for i in range(len(a) - 1):
        if a[i] in b:
            dubl.append(a[i])
        else:
            b.append(a[i])
    print(dubl)

def n3():
    x = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    n = int(input("Количество выходных дней: "))
    s1 = []
    s2 = []
    for i in range(n):
        s1.append(x[-i - 1])
    print("Ваши выходные дни: ", s1)
    for j in range(len(x)):
        if x[j] not in s1:
            s2.append(x[j])
    print("Ваши рабочие дни: ", s2)

def n4():
    s1 = ["Соловьёв", "Павлов", "Воробьёв", "Сергеев", "Карпов", "Крылов", "Беляев", "Тихомиров", "Фёдорова", "Рахманина"]
    s2 = ["Иванова", "Фёдоров", "Родченков", "Власов", "Кудрявцев", "Салохов", "Кузнецова", "Паймина", "Зотова", "Кузнецова"]
    elem1 = [0, 1, 6, 4, 9]
    elem2 = [2, 1, 5, 3, 8]
    x = []
    for i in elem1:
        x.append(s1[i])
    for i in elem2:
        x.append(s2[i])
    x = tuple(x)

    print("Группа 1: ", s1)
    print("Группа 2: ", s2)
    print("Состав команды: ", x)

    print("Длина команды: ", len(x))

    x = tuple(sorted(x))
    k = 0
    if "Иванов" in x:
        k = x.count("Иванов")
        print("Фамилия Иванов в кортеже встречается", k, "раз.")
    else:
        print("Фамилия Иванов в кортеже не встречается.")
print(n4())

