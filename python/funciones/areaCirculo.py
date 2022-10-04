import math

pi = math.pi
radio = 0.0
area = 0.0

print(' Calcula area de un circulo :')
print('Introduce el radio : ')
radio = input()


def areaCirculo(radio):
    return pi * math.pow(float(radio), 2)


area = areaCirculo(radio)

print('El area del circulo es', area)
