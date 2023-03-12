from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 
m = combinations(13, 4)
print(f'm = {m}');  
n=combinations(52, 4)
print(f'n = {n}')
P=m/n
print(f'P(4 крести) = {round(P,4)}')
n=combinations(52, 4)
print(f'n = {n}')
m=sum([combinations(4,1)*combinations(48,3),combinations(4,2)*combinations(48,2),combinations(4,3)*combinations(48,1),1])
print(f'm = {m}')
P=m/n
print(f'P(хотя бы 1 туз) = {round(P,4)}')

# Задача 2
P=1/combinations(10,3)
print(f'P(открыть с первой попытки) = {round(P,4)}')

# Задача 3
P=combinations(9,3)/combinations(15,3)
print(f'P(3 из 3-х окрашены) = {round(P,4)}')
# Задача 4
P=1/combinations(100,2)
print(f'P(оба выигрышных = {round(P,4)})')