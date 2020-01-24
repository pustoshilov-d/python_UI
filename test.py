import numpy as np
import math
from shell import shell

a = int(input('Введите а: '))
my_range = np.arange(2.6,7.4,0.5)
for x in my_range:
    print('x=', x,' a=',a, ' res=', math.sin(x)+a)
print()


a = [5.4, 3.1, 1.7, 0, 3, -5, -28]

count = 0
for i in a:
    if i >0:
        count += 1

print('Начальный массив: ',a)
print('Отсортированный: ',shell(a))
print('Положительных: ' , count)


i = 4432
print(str(i), i.__str__(), '{}'.format(i), "%s" % i)