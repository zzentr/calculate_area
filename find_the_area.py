
'''На счет вычисления фигуры в compile-time, я так понял на python это не сделать
т.к. он не компилируемый язык. Но вообще я бы сделал функцию, которая принимает кол-во
сторон и с помощью match-case, к примеру если 1 сторона, то значит это квадрат
и мы считаем его площадь и так далее'''



class Shape():
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):

        if self.radius < 0:
            raise ValueError('Радиус не может быть отрицательным')
        
        elif type(self.radius) not in (int, float):
            raise TypeError('Радиус должен быть числом')
        return 3.14 * self.radius ** 2
    

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        if any(not isinstance(num, (int, float)) for num in (self.a, self.b, self.c)):
            raise TypeError('Сторона должна быть числом')
        
        elif any(num <= 0 for num in (self.a, self.b, self.c)):
            raise ValueError('Сторона должна быть больше 0')

        elif self.a + self.b < self.c or self.b + self.c < self.a or self.c + self.a < self.b:
            raise ValueError('Неправильные размеры сторон треугольника')
        
        p = self.perimeter() / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 3)
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def is_right_triangle(self):
        sides = [self.a, self.b, self.c]
        hypotenuse = max(sides)
        sides.remove(hypotenuse)

        if sides[0] ** 2 + sides[1] ** 2 == hypotenuse ** 2:
            return True
        return False
