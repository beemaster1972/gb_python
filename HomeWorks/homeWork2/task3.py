# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.

n = 16
k = 0
while 2 ** k <= n:
    print(2 ** k)
    k += 1
