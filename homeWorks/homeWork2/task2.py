"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `list_1` и `k`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения
`list_1` и `k` для проверки
"""

list_1 = [1, 2, 3, 4, 5, 7, 8, 9]
k = 10

# Введите ваше решение ниже
count = 0
desired_value = list_1[0]
for element in list_1:
    if abs(element - k) < abs(desired_value - k):
        desired_value = element

print(desired_value)