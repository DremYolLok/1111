# A

while (fire := input() != "Три!"):
    print("Режим ожидания...")
print("Ёлочка, гори!")

# B

counter = 0
while (x := input()) != 'Приехали!':
    if 'зайка' in x:
        counter += 1
print(counter)

# C

counter = 0
while (x := input()) != 'Приехали!':
    if 'зайка' in x:
        counter += 1
print(counter)

# D

a = int(input())
b = int(input())
if a < b:
    while a != b + 1:
        print(a, end=' ')
        a += 1
else:
    while a != b - 1:
        print(a, end=' ')
        a -= 1

# E

price_of_product = float(input())
amount = 0
while price_of_product != int(0):
    if price_of_product < 500:
        amount += price_of_product
    elif price_of_product >= 500:
        amount += (price_of_product - (price_of_product / 100 * 10))
    price_of_product = float(input())
print(amount)

# F

a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)

# G

a = int(input())
b = int(input())
n = max(a, b)
while (n % min(a, b) != 0):
    n += max(a, b)
print(n)

# H

q = str(input())
n = int(input())
k = 0
while k != n:
    print(q)
    k += 1

# I

n = int(input())
k = 1
rez = 1
while k != n + 1:
    rez *= k
    k += 1
print(rez)

# J

x = 0
y = 0
while (n := str(input())) != 'СТОП':
    k = int(input())
    if n == 'СЕВЕР':
        x += k
    if n == 'ЮГ':
        x -= k
    if n == 'ЗАПАД':
        y -= k
    if n == 'ВОСТОК':
        y += k
print(f'{x}\n{y}')

# K

num = int(input())
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print(sum)

# L

num = int(input())
max = 0
while (num != 0):
    if num % 10 > max:
        max = num % 10
    num = num // 10
print(max)

# M

n = int(input())
name1 = 'Иштар'
for i in range(0, n):
    name2 = str(input())
    if name1 > name2:
        name1 = name2
print(name1)

# N

v = int(input())

d = 2
while d * d <= v and v % d != 0:
    d += 1
r = 'YES' if d * d > v and v != 1 else 'NO'

print(r)

# O

n = int(input())
k = 0
for i in range(0, n):
    s = str(input())
    if 'зайка' in s:
        k += 1
print(k)

# P

number = input()
rev = reversed(number)

if list(number) == list(rev):
    print("YES")
else:
    print("NO")
