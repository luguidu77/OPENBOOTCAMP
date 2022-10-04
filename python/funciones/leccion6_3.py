

class Alumno():
    nombre = 'nombre',
    nota = 0,

    def setNombre(self, nombre):
        self.nombre = nombre

    def setNota(self, nota):
        self.nota = nota


alumno = Alumno()
print('Nombre del alumno: ')
texto = input() 
print('Nota del alumno', texto, ': ')
nota = float(input())

alumno.setNombre(texto)
alumno.setNota(nota)

if nota >= 5:
    print('El alumno ', alumno.nombre, ', ha aprobado con una nota de ', nota)
else:
    print('El alumno ', alumno.nombre, ', ha suspendido con una nota de ', nota)
