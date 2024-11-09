# A

print("Привет, Яндекс!")

# B

print("Как Вас зовут?")
username = input()
print(f"Привет, {username}")

# C

name = input()
print(name)
print(name)
print(name)

# D

print(int(int(input()) - 2.5 * 38))

# E

price = int(input())
weight = int(input())
cash = int(input())
print(cash - price * weight)

# F

name = str(input())
x = int(input())
y = int(input())
u = int(input())
sum = x * y
sum2 = u - sum
print('Чек')
print(f'{name} - {y}кг - {x}руб/кг')
print(f'Итого: {sum}руб')
print(f'Внесено: {u}руб')
print(f'Сдача: {sum2}руб')

# G

a = int(input())
print(('Купи слона!' + '\n') * a)

# H

a = int(input())
b = input()
print(("Я больше никогда не буду писать \"" + b + "\"!\n") * a)

# I

N = int(input())
M = int(input())
a = N / 2
b = M * a
print(int(b))

# J

a = str(input())
b = int(input()) 
c = b // 10 // 10 % 10
d = b // 10 % 10 
e = b % 10 
print(f"Группа №{c}.")
print(f"{e}. {a}.")
print(f"Шкафчик: {b}.")
print(f"Кроватка: {d}.")

# K

cifry = int(input()) 
a = cifry // 1000 % 10
b = cifry // 100 % 10 
c = cifry // 10 % 10
d = cifry % 10 
print(f'{b}{a}{d}{c}')

# L

num1 = int(input()) 
num2 = int(input()) 
res1 = ((num1 % 10) + (num2 % 10)) % 10 
res2 = ((num1 // 10) + (num2 // 10)) % 10 
res3 = ((num1 // 100) + (num2 // 100)) % 10 
print(str(res3) + str(res2) + str(res1))

# M

deti = int(input())
konfety = int(input())
print(konfety // deti)
print(konfety % deti)

# N

k_sharik = int(input())
z_sharik = int(input())
s_sharik = int(input())
print(k_sharik + s_sharik + 1)

# O

a = int(input()) * 60
b = int(input())
d = int(input())
h = (a + b + d) // 60 % 24
m = (a + b + d) % 60
print(f'{h:02}:{m:02}')

# P

a = int(input())
b = int(input())
c = int(input())
print(f"{(b - a) / c}0")
