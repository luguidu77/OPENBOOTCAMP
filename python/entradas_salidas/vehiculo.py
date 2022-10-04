
import pickle


class Vehiculo:
    marca = ''
    modelo = ''

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def getvehiculo(self):
        return print(f'Vehiculo seleccionado es marca {self.marca}, modelo {self.modelo} ')


vehiculo = Vehiculo('Seat', 'Ibiza')

f = open('Vehiculo.bin', 'wb')
pickle.dump(vehiculo, f)
f.close

f = open('Vehiculo.bin', 'rb')
vehiculo = pickle.load(f)
f.close

print(vehiculo.getvehiculo())
