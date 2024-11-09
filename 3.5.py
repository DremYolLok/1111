# A

from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip(" \n"))

summa = 0
for string in lines:
    numbers = list(map(int, string.split()))
    for num in numbers:
        summa += num
print(summa)

# B

from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip(" \n"))

summa = 0
for line in lines:
    first = int(line.split()[1])
    second = int(line.split()[2])
    diff = second - first
    summa += diff
print(round(summa / len(lines)))

# C

from sys import stdin

for line in stdin:
    if not line.startswith("#"):
        code = line.split('#')[0]
        print(code.rstrip('\n'))

# D

from sys import stdin

lines = stdin.readlines()
query = lines[-1].rstrip('\n').lower()

for i in range(0, len(lines) - 1):
    line = lines[i]
    if query in line.lower():
        print(line.rstrip('\n'))

# E

from sys import stdin

data = [string.strip().split() for string in stdin]
words = []
for line in data:
    words.extend(line)
for word in sorted(set(words)):
    if word.lower() == word.lower()[::-1]:
        print(word)

# F

dictionary = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
              'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
              'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
              'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
              'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
              'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
              'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}


def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщыьэъюя')):
    return not alphabet.isdisjoint(text.lower())


with open("cyrillic.txt", "r", encoding="utf-8") as data:
    text = data.readlines()

with open("transliteration.txt", "a", encoding="utf-8") as translate:
    for word in text:
        for v in word:
            if v.isalpha() and match(v) is True:
                print(dictionary.get(v), end="", file=translate)
            elif not v.isalpha() or match(v) is False:
                print(v, end="", file=translate)

# G

name = input()
numbers = []
with open(name, 'r') as f:
    for line in f:
        numbers.extend([int(x) for x in line.split()])
print(len(numbers))
print(len(list(filter(lambda x: x > 0, numbers))))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers), 2))

# H

first = input()
second = input()
answer = input()

with open(first, "r", encoding="utf-8") as f:
    first_text = f.readlines()

with open(second, "r", encoding="utf-8") as s:
    second_text = s.readlines()

result_for_first = set()
for line in first_text:
    line_split = line.replace("\n", "").split()
    for word in line_split:
        result_for_first.add(word)

result_for_second = set()
for line in second_text:
    line_split = line.replace("\n", "").split()
    for word in line_split:
        result_for_second.add(word)

with open(answer, "a", encoding="utf-8") as a:
    set_answer = result_for_first ^ result_for_second
    for word in sorted(set_answer):
        print(word, file=a)

# I

from itertools import filterfalse

fin, fon = input(), input()

with open(fin, encoding='UTF-8') as fi:
    sss = fi.readlines()

so = '' 
for s in sss:
    sv1 = s.strip().rstrip('\n')
    sv2 = ''.join(sv1.split('\t'))
    sv3 = list(filterfalse(lambda x: x == '', sv2.split(' ')))
    sv4 = ' '.join(sv3)
    if sv4.strip() == '':
        continue
    so += sv4 + '\n'
    
with open(fon, 'w', encoding='UTF-8') as fo:
    fo.write(so)

# J

file_in, number = input(), int(input())
data = []
with open(file_in) as f:
    for line in f:
        data.append(line)
for line in data[-number:]:
    print(line.strip())
