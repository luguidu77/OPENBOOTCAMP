
import operaciones.restador.resta as r
import operaciones.sumador.suma as s
import operaciones.divisor.divide as d
import operaciones.multiplicador.multipica as m

a = 6
b = 2

def main():
    resta = r.resta(a, b)
    suma = s.suma(a, b)
    multiplica = m.multiplica(a, b)
    divide = d.divide(a, b)

    print('operaciones con los numeros', a ,'y' , b)
    print(' resta ' , resta, '\n suma ', suma ,'\n multiplicacion ' ,multiplica, '\n division ', divide)


if __name__ == '__main__':
    main()
