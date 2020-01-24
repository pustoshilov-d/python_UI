#1
print('My first program ahaha')

#2
import sys
try:
    print(sys.argv[1:][0])
except: print('Без аргументов')
#python L1.py "Привет, мир!"

#3
from L1_2 import sum
print(sum(5,5))

#4
A = "Глобальная переменная А"
from L1_2 import B
if True: C = "Локальная переменная С"; print(C)
print(A)
print(B)




