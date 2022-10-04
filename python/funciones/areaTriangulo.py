h = 0.0
b = 0.0
area = 0.0

print(' Calcula area de un triangulo :')
print('Introduce la altura : ')
h = input()
print('Introduce la base : ')
b = input()


def areaTriangulo(h, b):
    area = (h * b)/2
    print(" El area del triangulo es",  area)


areaTriangulo(20, 5)
