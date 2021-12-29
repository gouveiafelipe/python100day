number_str = '124489903108444899'
count_numbers = len(number_str)

# pegar o primeiro indice, somar com o proximo e verificar se ele se repete na string

print(len(number_str))
number_list = []


def numbers_loop():
    dictionary_numbers = {}
    contador = 0
    loop_count = 0
    x_index = 0
    y_index = 1
    teemo = ''
    for t in number_str:
        while loop_count < count_numbers:
            add_list = number_str[x_index: y_index]
            number_list.append(add_list)
            y_index += 1
            if y_index > count_numbers:
                x_index += 1
                y_index = 1
                loop_count = 0
                break
            loop_count += 1

    for teemo in number_list:
        if len(teemo) < 2 or None or '':
            number_list.remove(teemo)
        count_numbers_list = number_list.count(teemo)
        if count_numbers_list > 1:
            dictionary_numbers[teemo] = count_numbers_list
            contador += 1

    print(len(number_list[0:1]))
    print(number_list)
    print(dictionary_numbers)


numbers_loop()



# for n in number_list:
#     if len(n) < 2 or None or '':
#         number_list.remove(n)
#     count_numbers_list = number_list.count(n)
# if count_numbers_list > 1:
#     dictionary_numbers[n] = count_numbers_list
# contador += 1

