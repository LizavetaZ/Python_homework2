# Задача 4 - список различных чисел
# import random
# some_list = [random.randint(1,10) for i in range (8)]
# print(some_list)
# res = set(some_list)
# print(res)

#Задача 1 - фрукты
# k = int(input('введите количество фруктов: '))
# new_dict = {}
# for i in range (k):
#     fruitname = input('Введите название фрукта: ')
#     fruitquant = input('Введите количество названного фрукта: ')
#     new_dict.setdefault(fruitname, fruitquant)
# print(new_dict)


#Задача 2 - Старший и младший
# N = int(input('введите количество друзей: '))
# new_dict = {}
# for i in range (N):
#     friendname = input('Введите имя друга: ')
#     friendage = int(input('Введите возраст друга: '))
#     new_dict.setdefault(friendname, friendage)
# print(new_dict)
# x = min(new_dict, key=new_dict.get)
# print(x)


#Задача 3 - Еще немного о друзьях
# N = int(input('введите количество друзей: '))
# new_dict = {}
# for i in range (N):
#     friendname = input('Введите имя друга: ')
#     friendage = int(input('Введите возраст друга: '))
#     new_dict.setdefault(friendname, friendage)
# print(new_dict)
# summ = sum(new_dict.values())
# print('средний возраст: ', round(summ/len(new_dict), 2))
# name_list = []
# name_list = list(new_dict.keys())
# print('Самое длинное имя: ', max(name_list, key=len))


#Задача 4 - Английский словарь
N = int(input('введите количество слов: '))
new_dict = {}
for i in range (N):
    eng = input('Введите слово на английском: ')
    translate = (input('Введите варианты перевода: ')).split(',')
    new_dict.setdefault(eng, translate)
print(new_dict)