# A

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y   

# B

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)
    
# C

class RedButton:

    def __init__(self):
        self.c = 0

    def click(self):
        print('Тревога!') 
        self.c += 1

    def count(self): 
        return self.c 

# D

class Programmer:

    def __init__(self, name, position="Junior"):
        self.name = name
        self.position = position
        self.worked = 0
        self.money = 0
        self.overrises = 0

    def work(self, time):
        P = {
            "Junior": 10,
            "Middle": 15,
            "Senior": 20,
        }
        self.worked += time
        self.money += time * (P[self.position] + self.overrises)

    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
        elif self.position == "Middle":
            self.position = "Senior"
        elif self.position == "Senior":
            self.overrises += 1

    def info(self):
        return f'{self.name} {self.worked}ч. {self.money}тгр.'
    
# E

class Rectangle:

    def __init__(self, csa, csb):
        a = abs(csa[0] - csb[0]) 
        b = abs(csa[1] - csb[1])
        self.p = float(f'{2 * (a + b):.2f}')
        self.a = float(f'{a * b:.2f}')
    
    def perimeter(self):
        return self.p
    
    def area(self):
        return self.a    
