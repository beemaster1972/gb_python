# from math import ceil
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
n = 700
m = 500
# Output:
# 2
#
# n = int(input("Сколько км проезжает за день: "))
# m = int(input("Сколько км маршрут: "))

print(f'{m} км проедет за {(n+m-1)//n} дня')