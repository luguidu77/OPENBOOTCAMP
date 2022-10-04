class Vehiculo():
    color = 'rojo'
    ruedas = 4
    puertas = 2


class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 2.0


coche = Coche()
print('Mi coche : ')
print('Color: ', coche.color)
print('Nº de ruedas: ', coche.ruedas)
print('Nº de puertas: ', coche.puertas)
print('Velocidad max: ', coche.velocidad)
print('Cilindrada: ', coche.cilindrada)
