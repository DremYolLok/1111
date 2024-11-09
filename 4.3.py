# A

def recursive_sum(*numbers):
    if not numbers:
        return 0
    return numbers[-1] + recursive_sum(*numbers[:-1])

# B

def recursive_digit_sum(number):
    if number // 10 == 0:
        return number
    last_digit = number % 10
    return last_digit + recursive_digit_sum(number // 10)

# C

def make_equation(*args):
    if len(args) == 1:
        return args[0]
    return f'({make_equation(*args[:len(args) - 1])}) * x + {args[-1]}'

# D

def answer(func):
    def wrap(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return wrap

# E

def result_accumulator(func):
    result = []

    def wrap(*args, method="accumulate"):
        result.append(func(*args))
        if method == "drop":
            temp = result.copy()
            result.clear()
            return temp
    return wrap
