# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = 5
m = 3
k = 15
print(
    f'От шоколадки размерностью {n} на {m} {"можно" if (not k % n or not k % m) and k < n * m else "нельзя"} отломить {k} долек')
