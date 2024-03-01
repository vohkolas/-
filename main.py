import random

list1 = ["Иван", "Пётр", "Фёдор", "Матвей", "Даниил", "Александр"]
list2 = ["Анна", "Ирина", "Вера", "Ульяна", "Нина", "Елизавета"]

for i in list2:
    list1.append(i)

amount = random.randint(0, len(list1) - 1)

tuple = tuple((random.sample(list1, amount)))
print(tuple)

name = input()

if name in tuple:
    print('True. Студент', name, 'встречается в кортеже.')
else:
    print('False. Студент', name, 'не найден.')