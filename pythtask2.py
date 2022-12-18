# N=float(input()) #Задача№14 - сумма цифр вещественного числа
# N_str=str(N)
# N_str=N_str.replace('.','')
# N_int=int(N_str)
# Sum=0
# while N_int!=0:
#     last_digit=N_int%10
#     Sum+=last_digit
#     N_int=N_int//10
# print(Sum)

# N=int(input())  #Задача 15 - произведение от 1 до N
# multiply=1
# for i in range(1,N):
#     multiply*=i
#     print(f'{multiply}', end=',')
# print(f'{multiply*(N)}')

# n=int(input())  #Задача 16 - самму из n чисел последовательности (1+1/n)**n
# list_n=[]
# for i in range(1, n+1):
#     list_n.append(round(((1+1/i)**i),2))
# print(list_n, sep=',')
# Sum=0
# for i in range(0,n):
#     Sum+=list_n[i]
# print(Sum)

# list_n=[]   #Задача 18 - перемешивание списка
# n=int(input('Введите количество элементов массива '))
# for i in range(0,n):
#     list_n.append(int(input('Введите элементы массива,нажимая ENTER после каждого элемента ')))
# print(list_n)
# import random
# random.shuffle(list_n)
# print(list_n)