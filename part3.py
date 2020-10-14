def my_compare(a, b, c):
    lst = [a, b, c]
    min_num = min(lst)
    lst.remove(min_num)
    return sum(lst)


print(f'Сумма двух наибольших чисел: {my_compare(2, 3, 6)}')
