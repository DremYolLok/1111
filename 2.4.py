# A

number = int(input())
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f"{i * j}", end=" ")
    print()

# B

number = int(input())
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f'{j} * {i} = {i * j}')

# C

number = int(input())
q = 1
s = 1
k = 0
while q <= number:
    print(q, end=' ')
    q += 1
    k += 1
    if k == s: 
        print()
        s += 1 
        k = 0

# D

number = int(input())
sum = 0
for i in range(number):
    temp = int(input())
    while temp != 0:
        sum += temp % 10
        temp //= 10
print(sum)

# E

number = int(input())
rabbit_is_true = [] 
for i in range(number):
    counter = 0 
    temp = input()
    while temp != "ВСЁ": 
        if "зайка" in temp: 
            counter += 1
            if counter == 1: 
                rabbit_is_true.append("зайка") 
        temp = input()
print(rabbit_is_true.count("зайка"))

# F

n, a = int(input()), int(input())
for _ in range(n - 1):
    b = int(input())
    while b:
        a, b = b, a % b
print(a)

# G

n = int(input())
count = 1

for a in range(n):
    for b in range(3 + count, 1, -1):
        print(f'До старта {b - 1} секунд(ы)')

    print(f'Старт {count}!!!')

    count += 1

# H

name, summ = '', 0
for _ in range(int(input())):
    temp_name, temp_summ = input(), sum(map(int, input()))
    if temp_summ >= summ:
        name, summ = temp_name, temp_summ
print(name)

# I

number = ''
for _ in range(int(input())):
    number += max(input())
print(number)

# J

number = int(input())
print("А Б В")
for i in range(1, number):
    for j in range(1, number):
        for k in range(1, number):
            if number - (i + j + k) == 0:
                print(i, j, k)

# K

n = int(input())
count = 0

for num in range(n):
    number = int(input())

    if number <= 1:
        continue

    flag = True
    k = number - 1

    while k > 1:
        if number % k == 0:
            flag = False
            break
        k -= 1

    if flag:
        count += 1


print(count)

# L

n = int(input())
m = int(input())
temp = 1
for i in range(n):
    for j in range(m):
        if n * m < 10:
            print("{:1}".format(temp), end=" ")
        elif n * m > 10 and n * m < 100:
            print("{:2}".format(temp), end=" ")
        else:
            print("{:3}".format(temp), end=" ")
        temp += 1
    print()

# M

height = int(input())
width = int(input())

cell_width = len(str(width * height))

number = 1
for row in range(height):
    number = row + 1
    for _ in range(width):
        print(f'{number:>{cell_width}}', end=' ')
        number += height
    print()

# P

n, m = int(input()), int(input())
delv = '|'
st = '-' * (n * m + n - 1)

for i in range(1, n + 1):
    for j in range(i, i * n, i):
        print(f'{j: ^{m}}', end=delv)
    print(f'{(i * n): ^{m}} ')
    if i < n:
        print(st)

# Q

counter = 0
for _ in range(int(input())):
    if (n := input()) == n[::-1]:
        counter += 1
print(counter)

# T

n = int(input())

k = 10
s = 0
for i in range(10, 1, -1):
    v = n
    km = 1
    sm = 0
    while v >= km * i:
        km *= i
    while v > 0:
        a = v // km
        sm += a
        v -= a * km
        km //= i
    if s <= sm:
        k = i
        s = sm
print(k)   
