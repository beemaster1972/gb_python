"""
Рекурсивная сумма

Инструкция по использованию платформы



Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

Функция не должна ничего выводить, только возвращать значение.

Пример:


sum(2, 2)
# 4
"""

def sum(a,b):
    if b == 0:
        return a
    return sum(a,b-1)+1
print(sum(33,34))