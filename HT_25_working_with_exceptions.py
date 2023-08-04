import math


class MyException(Exception):
    pass


class MyCalculator:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def add(self, a=None, b=None):
        try:
            num1 = self.num1 if a is None else a
            num2 = self.num2 if b is None else b
            if not str(num1).isdigit() or not str(num2).isdigit():
                raise MyException("Аргументы должны быть числами")
            res = int(num1) + int(num2)
            return res
        except MyException as error:
            return error

    def subtract(self, a=None, b=None):
        try:
            num1 = self.num1 if a is None else a
            num2 = self.num2 if b is None else b
            if not str(num1).isdigit() or not str(num2).isdigit():
                raise MyException("Аргументы должны быть числами")
            res = int(num1) - int(num2)
            return res
        except MyException as error:
            return error

    def multiplication(self, a=None, b=None):
        try:
            num1 = self.num1 if a is None else a
            num2 = self.num2 if b is None else b
            if not str(num1).isdigit() or not str(num2).isdigit():
                raise MyException("Аргументы должны быть числами")
            res = int(num1) * int(num2)
            return res
        except MyException as error:
            return error

    def division(self, a=None, b=None):
        try:
            num1 = self.num1 if a is None else a
            num2 = self.num2 if b is None else b
            if not str(num1).isdigit() or not str(num2).isdigit():
                raise MyException("Аргументы должны быть числами")
            if int(num2) == 0:
                raise MyException("Деление на ноль недопустимо")
            res = int(num1) / int(num2)
            return res
        except MyException as error:
            return error

    def exponentiation(self, a=None, b=None):
        try:
            num1 = self.num1 if a is None else a
            num2 = self.num2 if b is None else b
            num1 = int(num1)
            num2 = int(num2)
            if num2 < 0:
                raise MyException("Возведение в отрицательную степень недопустимо")
            res = num1 ** num2
            return res
        except MyException as error:
            return error

    def root_extraction(self, a=None):
        try:
            num1 = self.num1 if a is None else a
            num1 = int(num1)
            if num1 < 0:
                raise MyException("Извлечение корня из отрицательного числа недопустимо")
            res = math.sqrt(num1)
            return res
        except MyException as error:
            return error


my_object = MyCalculator(10, 5)

print(my_object.add())
print(my_object.subtract())
print(my_object.multiplication())
print(my_object.division())
print(my_object.exponentiation())
print(my_object.root_extraction(25))
