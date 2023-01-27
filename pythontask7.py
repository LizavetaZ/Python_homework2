#Задача1 - кофе
# ingredient = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0],
#               'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],
#               'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}
 
 
# def choose_coffee(preferences):
#     for i in preferences:
#         if ingredient[i][0] <= ingredients[0] and ingredient[i][1] <= ingredients[1] \
#                 and ingredient[i][2] <= ingredients[2]:
#             ingredients[0] -= ingredient[i][0]
#             ingredients[1] -= ingredient[i][1]
#             ingredients[2] -= ingredient[i][2]
#             return i
#     return 'К сожалению, не можем предложить Вам напиток'
 
 
# ingredients = [4, 4, 0]
# print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
# print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
# print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))

#Задача2 - шифр
def ceasar_encode(msg, shift):
    if msg.isalpha():
        number = ord(msg) + shift % 32
        if number > 1103:
            number -= 32
        return chr(number)
    return msg
 
 
shift = int(input())
for l in input():
    print(ceasar_encode(l, shift), end='')