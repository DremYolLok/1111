# A

string = input().split(" ")
for index, value in enumerate(string, 1):
    print(f'{index}. {value}')

# B

kids = list(zip(input().split(", "), input().split(", ")))
for i in kids:
    print(" - ".join(i))

# C

from itertools import count
values = [float(x) for x in input().split()]
for value in count(values[0], values[2]):
    if value > values[1]:
        break
    print(round(value, 2))

# D

from itertools import accumulate
string = input().split(" ")
for word in accumulate(string, lambda s1, s2: s1 + ' ' + s2):
    print(word)

# E

items = set()
for _ in range(3):
    items = items.union({item for item in input().split(', ')})
for i, item in enumerate(sorted(items), start=1):
    print(f'{i}. {item}')

# F

from itertools import product

nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())
for card in product(nominal, suits):
    print(card[0], card[1])

# G

from itertools import product
players, games = [], []
for _ in range(int(input())):
    players.append(input())
for i in product(players, players):
    if i[0] != i[1] and [i[1], i[0]] not in games:
        games.append([i[0], i[1]])
        print(f'{i[0]} - {i[1]}')

# H

cereals = []
for _ in range(int(input())):
    cereals.append(input())
amount = int(input())
cereals *= amount // len(cereals) + 1
for i in range(amount):
    print(cereals[i])

# I

from itertools import product
table_size = int(input())
numbers = [number for number in range(1, table_size + 1)]
for first_number, second_number in product(numbers, numbers):
    if second_number != table_size:
        print(first_number * second_number, end=' ')
    else:
        print(first_number * second_number)

# J

number = int(input())
print("А Б В")
for i in range(1, number):
    for j in range(1, number):
        for k in range(1, number):
            if number - (i + j + k) == 0:
                print(i, j, k)
                