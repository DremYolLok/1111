# A

def print_hello(name):
    print(f'Hello, {name}!')  

# B

def gcd(first_number, second_number):
    max_number = max(first_number, second_number)
    min_number = min(first_number, second_number)

    while (remainder := max_number % min_number) != 0:
        max_number = min_number
        min_number = remainder

    return min_number

# C

def number_length(number: int):
    if number >= 0:
        return len(str(number))
    else:
        return len(str(number)) - 1
    
# D

MONTHS = {
    'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
           'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December']
}


def month(month_position, locale):
    return MONTHS[locale][month_position - 1]

# E

def split_numbers(numbers):
    return tuple(int(number) for number in numbers.split())
