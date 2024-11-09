# A

print("Как Вас зовут?")
a = input()
print(f"Здравствуйте, {a}!")
print("Как дела?")
b = input()
if b == "хорошо":
    print("Я за вас рада!")
if b == "плохо":
    print("Всё наладится!")

# B

a = int(input()) 
b = int(input())
if (a > b):
    print("Петя")
else:
    print("Вася")

# C

a = int(input())
b = int(input())
c = int(input())
if (a > b and a > c):
    print("Петя")
elif (b > a and b > c):
    print("Вася")
else:
    print("Толя")

# D

p = int(input())
v = int(input())
t = int(input())
name_1 = max(p, v, t)
name_3 = min(p, v, t)
name_2 = p + v + t - max(p, v, t) - min(p, v, t)
if name_1 == p:
    print('1. Петя')
elif name_1 == t:
    print('1. Толя')
else:
    print('1. Вася')
if name_2 == p:
    print('2. Петя')
elif name_2 == t:
    print('2. Толя')
else:
    print('2. Вася')
if name_3 == p:
    print('3. Петя')
elif name_3 == t:
    print('3. Толя')
else:
    print('3. Вася')

# E

a = 7
b = 6
a1 = a - 3 + 2
b1 = b + 3 + 5 - 2
a2 = int(input())
b2 = int(input())
sum = a1 + a2
sum2 = b1 + b2
if (sum > sum2):
    print("Петя")
else:
    print("Вася")

# F

year = int(input())
if year % 4 or not year % 100 and year % 400:
    print('NO')
else:
    print('YES')

# G

n = int(input())
m = str(n)[::-1]
if str(n) == m:
    print('YES')
else:
    print('NO')

# H

forest = input()
print('YES') if 'зайка' in forest else print('NO')

# I

name1 = input()
name2 = input()
name3 = input()
print(min(name1, name2, name3))

# J

number = input()
first = int(number[0]) + int(number[1])
second = int(number[1]) + int(number[2])
print(str(first) + str(second)) if first > second else print(str(second) + str(first))

# K

number = list(map(int, input()))
first = max(number) + min(number)
print('YES') if first == 2 * (sum(number) - first) else print('NO')

# L

number = int(input())
number2 = int(input())
number3 = int(input())
if (number < number2 + number3 and number2 < number + number3 and number3 < number + number2):
    print("YES")
else:
    print("NO")

# M

number = int(input())
number2 = int(input())
number3 = int(input())
a = number // 10 % 10
b = number % 10
c = number2 // 10 % 10
d = number2 % 10
e = number3 // 10 % 10
f = number3 % 10
if (a == c and a == e):
    print(a)
elif (b == d and b == f):
    print(b)

# O

n = int(input())
m = int(input())
a = n % 10
b = n // 10 % 10
c = m % 10
d = m // 10 % 10
sr = (a + b + c + d - max(a, b, c, d) - min(a, b, c, d)) % 10
print(f'{max(a, b, c, d)}{sr}{min(a, b, c, d)}')

# R

sides = [int(input()), int(input()), int(input())]
sides.sort()
if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
    print('100%')
elif sides[2] ** 2 > sides[0] ** 2 + sides[1] ** 2:
    print('велика')
else:
    print('крайне мала')

# T

places = [input(), input(), input()]
places.sort()
for place in places:
    if 'зайка' in place:
        print(place, len(place))
        break
