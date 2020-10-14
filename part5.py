def my_sum():
    sum_res = 0
    ex = False
    while not ex:
        number = input('Введите строку чисел, разделенных пробелом. q - выход из программы - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма равна {sum_res}')
    print(f'По итогу сумма чисел равна {sum_res}')


my_sum()
