"""
Задача №1.

Дано п’ять цілих чисел a, b, c, d, e. Визначити, скільки з них додатних.

Автор: Костючик Валерія Дмитрівна
"""

a = int(input("Введіть число: "))
b = int(input("Введіть число: "))
c = int(input("Введіть число: "))
d = int(input("Введіть число: "))
e = int(input("Введіть число: "))

dot = 0

if a > 0:
    dot +=1
if b > 0:
    dot +=1
if c > 0:
    dot +=1
if d > 0:
    dot +=1
if e > 0:
    dot +=1

print("Кількість додатніх чисел:", dot)
