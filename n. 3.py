def n1():
    n = int(input())
    s = ''
    for i in range(n):
        x = input()
        s = s + x + ' '
    print(s)

def n2():
    s = ''
    while True:
        x = input()
        if x == 'stop':
            break
        s = s + x + ' '
    print(s)

def n3():
    x = input()
    k = 0
    for i in range(len(x)):
        if x[i] == 'ф' or x[i] == 'Ф':
            k = 1
    if k == 1:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень рекое слово...")
def n4():
    import random
    k = 0
    t = 0
    while k != 3:
        x = random.randint(0,10)
        y = random.randint(0,10)
        n = int(input(str(x) + '+' + str(y) + '='))
        print(x + y)
        if n != (x + y):
            print("Ответ неверный.")
            k += 1
        else:
            print("Правильно!")
            t += 1
    print("Игра окончена. Правильных ответов:", t)

print(n4())