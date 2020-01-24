import math
A, B, C = map(float,input("Введите A,B,C: ").split())
P = (A+B+C)/2
try: S = math.sqrt(P*(P-A)*(P-B)*(P-C))
except: print("Корня не существует")
print(S)