def my_division(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"


print(f'Результат деления: {my_division (float(input("Введите первое число: ")), float(input("Введите второе число: ")))}')
