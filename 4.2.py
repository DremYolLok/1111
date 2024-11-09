# A

def make_list(length, value=0):
    return [value] * length

# B

def make_matrix(size, value=0):
    if isinstance(size, tuple):
        return [[value] * size[0] for _ in range(size[1])]
    else:
        return [[value] * size for _ in range(size)]
    
# C

def gcd(*values):
    a = values[0]
    for i in range(1, len(values)):
        b = values[i]
        while b != 0:
            (a, b) = (b, a - b) if a > b else (a, b - a)
    return a        

# D

def month(number, language='ru'):
    MONTH = {
        'en': [
            'January', 'February', 'March',
            'April', 'May', 'June',
            'July', 'August', 'September',
            'October', 'November', 'December'
        ],
        'ru': [
            'Январь', 'Февраль', 'Март',
            'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь',
            'Октябрь', 'Ноябрь', 'Декабрь'
        ]
    }
    return MONTH[language][number - 1]

# E

def to_string(*data, sep=' ', end='\n'):
    preparation = map(lambda x: str(x), data)
    result = sep.join(preparation) + end
    return result
