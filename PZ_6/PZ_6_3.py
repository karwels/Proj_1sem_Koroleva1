#Дан список размера N. Осуществить сдвиг элементов список вправо на одну
#позицию (при этом A1 перейдет в A2, A2 — в A3, ..., AN-1 — в AN, a исходное значение
#последнего элемента будет потеряно). Первый элемент полученного списка
#положить равным 0.
import random
try:
  N = random.randrange(1,20)
except ValueError:
  print('Ошибка')
print("N = ", N)
a = [i for i in range(N)]
print("Массив:\n",a)
print("Массив со сдвигом  на 1:\n", a[1:] + [0])