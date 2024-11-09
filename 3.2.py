# A

s = input()
v = ''.join(set(s))
print(v)

# B

str1 = set(input()) 
str2 = set(input()) 
str_intersection = str1 & str2 
for i in str_intersection: 
    print(i, end="") 

# C

n = int(input()) 
set_1 = set() 
for i in range(n): 
    string = input().split(" ") 
    for j in string: 
        set_1.add(j) 
for k in set_1: 
    print(k) 

# D

N = int(input())
M = int(input())
result = [] 
counter = 0 
for i in range(N): 
    secondname = input()  
    result.append(secondname) 
for i in range(M): 
    secondname = input() 
    if secondname not in result: 
        result.append(secondname) 
    else:
        counter += 1 
print(counter if counter > 0 else "Таких нет") 

# E

N = int(input())
M = int(input())
result = list()
counter = 0
for i in range(N + M):
    secondname = input()
    if secondname not in result:
        result.append(secondname)
        counter += 1
    else:
        counter -= 1
print(counter if counter > 0 else "Таких нет")

# F

N = int(input())
M = int(input())
set_1 = set()
for i in range(N + M):
    secondname = input()
    if secondname not in set_1:
        set_1.add(secondname)
    else:
        set_1.remove(secondname)
if len(set_1) > 0:
    for x in sorted(set_1):
        print(x)
else:
    print("Таких нет")

# G

dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
              'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.'}
text = input().upper().split(" ")
for word in text:
    for v in word:
        print(dictionary.get(v), end=" ")
    print()

# H

N = int(input())
kasha = dict()
for i in range(N):
    secondname = input().split(" ")
    name = secondname[0]
    kasha_keys = secondname[1:]
    for each in kasha_keys:
        if each not in kasha:
            kasha[each] = [name]
        else:
            kasha[each].append(name)
selected_kasha = input()
answer = []
if selected_kasha in kasha:
    for i in range(len(kasha[selected_kasha])):
        answer.append(kasha[selected_kasha][i])
else:
    print("Таких нет")
for j in sorted(answer):
    print(j)

# I

dct = {}
while True:
    rabbit = input()
    temp = rabbit.split(" ")
    for r in temp:
        if r not in dct:
            dct[r] = 0
        dct[r] += 1
    if rabbit == "":
        break
for key, value in dct.items():
    if key != "":
        print(key, value)

# J

d = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TC',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Э': 'E', 
    'Ю': 'IU', 
    'Я': 'IA'
}

s = input()
for ci in s:
    if "ьъЬЪ".find(ci) != -1:
        continue
    ciu = ci.upper() 
    if ciu in d:
        if ci.isupper() is True:
            eci = d[ciu].capitalize()
        else:
            eci = d[ciu].lower()    
    else:
        eci = ci        

    print(eci, end='')
     