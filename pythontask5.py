#задача 1 - искл слова с абв

# some_list = ['роща', 'лес', 'сосна', 'ель', 'дуб', 'вишня', 'яблоко', 'еж', 'зубр']
# new_list=list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, some_list))
# print(new_list)

#задача 4 - алгоритм RLE
string_arr = "aaaaaaaabbbbbbbbbaadddddddddaaafffffff  aaccaassssaa  ff ss a"
count = 0    #8a9b2a9d3a7f2 2a2c2a4s2a2 2f1 2s1 1a
index = 0
size = len(string_arr)
find_index = 0
res = []
res2 = []
res3 = ""
while index < size:
    count = 0
    while find_index < size:
        if string_arr[index] == string_arr[find_index]:
            count += 1
        else:
            break
        find_index += 1
    res.append((count, string_arr[index]))
    res2.append(f"{count}{string_arr[index]}")
    res3 += f"{count}{string_arr[index]}"
    index = find_index

print(res)
print(res2)
print(res3)