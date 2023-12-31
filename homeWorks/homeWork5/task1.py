"""
Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

Функция не должна ничего выводить, только возвращать значение.

Пример:


a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8
"""

a = 2
b = 3
def rec_pow(base, exponent):
    if exponent == 0:
        return 1
    return rec_pow(base,exponent-1)*base
print(rec_pow(a,b))