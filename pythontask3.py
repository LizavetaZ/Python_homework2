# Задача 1 - сумма элементов списка на нечетных позициях
# a = input().split(', ')
# sum = 0
# for i in range(len(a)):
#     if i % 2 != 0:
#         sum+=int(a[i])
# print(sum)

#Задача 1 - произведение пар чисел
# a = input().split(', ')
# for i in range(len(a)//2):
#     print(int(a[i])*int(a[-1-i]))
# if len(a)%2!=0:
#     print(int(a[len(a)//2])**2)

#Задача 1 - разницу между максимальным и минимальным значением дробной части элементов - взяла у вас, в моих решениях все портит куча знаков после запятой
# some_list = input().split()
# maxx = 0
# minn = 1
# for el in some_list:
#     if float(el) % 1 != 0:
#         if float(el) % 1 < minn:
#             minn = float(el) % 1
#         if float(el) % 1 > maxx:
#             maxx = float(el) % 1
# print(round(maxx - minn, 2))

#Задача 1 - преобразоваие двоичного числа в десятичное
# a = int(input())
# some_list = []
# while a > 0:
#     some_list.append(str(a % 2))
#     a//=2 #не получалось с этой строчкой, списала у вас)
# some_list.reverse()
# print(*some_list, sep='')

