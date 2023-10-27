# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

num = 123006
ticket = num
digits = []

while num:
    digits.append(num % 10)
    num //= 10
print(f"Билет № {ticket} {'Счастливый' if sum(digits[:3]) == sum(digits[3:]) else 'Несчастливый'}")
