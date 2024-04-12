import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to(self, ot_point):
        return math.sqrt((self.x - ot_point.x)**2 + (self.y - ot_point.y)**2)

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

#1 задание
input_list = [1, 2, 2, 3, 4, 5, 5]
out_list=set(input_list)
print(out_list)
#2 задание
print("Введение 1 число")
a=int(input())
print("Введите 2 число")
b=int(input())
prime_numbers = []
for num in range(a, b + 1):
    if is_prime(num):
        prime_numbers.append(num)
print(prime_numbers)

#3 задание
point1 = Point(0, 0)
point2 = Point(3, 4)
print(point1.distance_to(point2))
print(point1.get_coordinates())
point1.set_coordinates(5, 5)
print(point1.get_coordinates())

#4 задание

array = []
n = int(input("Введите размер массива: "))
for i in range(n):
    element = str(input(f"Введите элемент {i + 1}: "))
    array.append(element)
    
sort_key = lambda s: (-len(s), s)
array.sort(key=sort_key)
print(array)
array.reverse()
print(array)