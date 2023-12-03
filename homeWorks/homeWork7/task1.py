"""
Напишите функцию print_operation_table(operation, num_rows, num_columns),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
как например, у операции умножения.

Пример

На входе:


print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:


1 2 3
2 4 6
3 6 9
"""
MIN_VAL = 2


def validate_coords(x, y):
    condition = [x >= MIN_VAL, y >= MIN_VAL]
    return all(condition)
#     if not all(condition):
#         raise ValueError("ОШИБКА! Размерности таблицы должны быть больше 2!")


def print_operation_table(operation, num_rows, num_columns):
    if validate_coords(num_rows, num_columns):
        print(*list(range(1,num_columns+1)))
        for row in range(2, num_rows + 1):
            print(row, *[operation(row, column) for column in range(2, num_columns + 1)])
    else:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")

print_operation_table(lambda x, y: x / y, 4, 4)
