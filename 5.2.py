# A

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, a, b):
        self.x += a
        self.y += b    

    def length(self, p):
        lv = ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5 
        return self.norm(lv)  

    def norm(self, value):
        return float(f'{value:.2f}')      


class PatchedPoint(Point):

    def __init__(self, *args): 
        match len(args):
            case 0:
                super().__init__(x=0, y=0)
            case 1:
                super().__init__(args[0][0], args[0][1])
            case 2:
                super().__init__(args[0], args[1])

# B

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 2:
            x, y = args
            super().__init__(x, y)
        else:
            x, y = args[0]
            super().__init__(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'
    
# C

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self
    
# D

class Fraction:

    def __simp(self, coords):
        a, b = coords[0], coords[1]
        while b:
            a, b = b, a % b
        return coords[0] // a, coords[1] // a

    def __init__(self, *args):
        if isinstance(args[0], str):
            self.n, self.d = self.__simp(tuple(map(int, args[0].split('/'))))
        else:
            self.n, self.d = self.__simp(args)

    def numerator(self, number=0):
        if number:
            self.n, self.d = self.__simp((number, self.d))
        return self.n

    def denominator(self, number=0):
        if number:
            self.n, self.d = self.__simp((self.n, number))
        return self.d

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction({self.n}, {self.d})"
    
# E

class Fraction:

    def __init__(self, *args):
        match len(args):
            case 1:
                ss = args[0].split("/")
                self.n = int(ss[0])
                self.d = int(ss[1])  
            case 2:
                self.n = int(args[0])
                self.d = int(args[1])    

        if self.d < 0:
            self.n = int(-self.n)
            self.d = int(-self.d)

        self.__simplify() 

    def numerator(self, number=None):
        if number is None:
            return abs(self.n)
        
        if self.n < 0:
            self.n = int(-number)   
        else:
            self.n = int(number)
        
        if number:
            self.__simplify()    

    def denominator(self, number=None):
        if number is None:
            return self.d

        if number < 0:
            self.n = int(-self.n)   
            self.d = int(-number) 
        else:
            self.d = int(number)
        
        self.__simplify()        

    def __simplify(self):
        a, b = abs(self.n), abs(self.d)
        while b:
            a, b = b, a % b
        
        self.n //= a 
        self.d //= a   

    def __neg__(self):
        return Fraction(-self.n, self.d)

    def __str__(self):
        return f'{self.n}/{self.d}'    

    def __repr__(self):
        return f"Fraction('{self.n}/{self.d}')" 

