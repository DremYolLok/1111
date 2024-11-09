# A

number = int(input())
counter = 0
for i in range(number):
    temp = input()
    list_temp = list(temp)
    if list_temp[0] == "а" or list_temp[0] == "б" or list_temp[0] == "в":
        counter += 1
if counter == number:
    print("YES")
else:
    print("NO")

# B

for i in input():
    print(i)

# C

length = int(input())
for _ in range(int(input())):
    line = input()
    print(line[:length - 3].ljust(length, ".") if len(line) > length else line)

# D

while (n := input()):
    if not n.endswith('@@@'):
        if n.startswith('##'):
            print(n[2:])
        else:
            print(n)

# E

string = input()
rev = reversed(string)
if list(string) == list(rev):
    print("YES")
else:
    print("NO")

# F

number = int(input())
counter = 0
for i in range(number):
    temp = input()
    counter += temp.count("зайка") 
print(counter)

# G

s = input()
sv = 0
for v in s.split(' '):
    sv += int(v)
print(sv)

# H

number = int(input())
list_temp = []
for i in range(number):
    temp = input()
    list_temp.append(temp)
for string in list_temp:
    if "зайка" in string:
        print(string.index("зайка") + 1)
    else:
        print("Заек нет =(")

# I

while (s := input()) != '':
    k = s.find('#')
    match k:
        case -1:
            print(s)
        case 0:
            continue
        case _:
            print(s[:k])

# J

answer = "" 
counter = 0 
dct = {}
while True:
    temp = input()
    n = temp.upper()
    for now in n:
        if now not in dct:
            dct[now] = 0
        dct[now] += 1
    for key in dct:
        if key != " ":
            if dct[key] > counter:
                counter = dct[key]
                answer = key
            elif dct[key] == counter:
                if key < answer:
                    answer = key 
    if temp == "ФИНИШ":
        break
print(answer.lower())

