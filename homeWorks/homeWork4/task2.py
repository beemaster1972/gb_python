"""
Черника

Инструкция по использованию платформы

В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены
по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.

Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов.
Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий
модуль за один заход, находясь перед некоторым кустом грядки.

Входные данные:

На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники.
Размер списка не превышает 1000 элементов.

Выходные данные:

Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль,
находясь перед некоторым кустом грядки.
"""

arr = [5, 8, 6, 4, 9, 2, 7, 8]
arr = [10, 8, 6, 4, 2]
number_of_bushes = len((arr))
harvest_from_three_blueberry_bushes = [sum(arr[i - 1:i + 2 if i < number_of_bushes - 1 else 0]) for i in
                                       range(number_of_bushes)]
harvest_from_three_blueberry_bushes[0] = arr[-1] + arr[0] + arr[1]
harvest_from_three_blueberry_bushes[-1] = arr[-2] + arr[-1] + arr[0]
print(*harvest_from_three_blueberry_bushes)
print(max(harvest_from_three_blueberry_bushes))
