def my_func(x, y):
    return x ** y


def my_func_while(x, y):
    r = 1
    while y < 0:
        r *= x
        y += 1
    return 1 / r


def my_func_rec(x, y):
    y = abs(y)
    if y == 0:
        return 1
    else:
        return 1 / x * my_func_rec(x, y - 1)


a = 15
b = -3
print(my_func(a, b))
print(my_func_while(a, b))
print(my_func_rec(a, b))
