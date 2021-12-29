def numbers_loop():
    a = 0
    b = 2
    c = 0
    d = 3
    contador = 0
    dictionary_numbers = {}
    while contador < count_numbers:
        index_2 = number_str[a:b]
        number_list.append(index_2)
        a += 1
        b += 1
        if len(index_2) < 2:
            number_list.remove(index_2)

        index_3 = number_str[c:d]
        number_list.append(index_3)
        c += 1
        d = c + 3
        if len(index_3) < 3:
            number_list.remove(index_3)

        for i in number_list:
            count = number_list.count(i)
            if count > 1:
                dictionary_numbers[i] = count
        contador += 1
    print(number_list)
    print(dictionary_numbers)
numbers_loop()