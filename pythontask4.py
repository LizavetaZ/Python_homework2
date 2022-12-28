#Задача1 - Вычислить число c заданной точностью d
import math
a = math.pi
print(a)
count = 0
d = float(input())
while d%1!= 0:
    d = d*10
    count += 1
print(count)
print(round(a, count))


# Задача1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def is_prime(num):
#     for i in range(2,(num//2)):
#         if num%i==0:
#             return False
#     return True

# a = int(input())
# some_list = []
# final_list = []
# for i in range(1, a):
#     if a % i == 0:
#         some_list.append(i)

# print(*some_list, sep=", ")

# for j in some_list:
#     if is_prime(j):
#         final_list.append(j)

# print(final_list)

# Задача2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
# some_list = input().split(' ')
# res = []
# for i in range(len(some_list)):
#     a = some_list.count(some_list[i])
#     if  a<2:
#         res.append(some_list[i])
# print(res)