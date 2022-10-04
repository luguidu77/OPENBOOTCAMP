from datetime import datetime

actual = datetime.now().hour
horarioFinal = 19



if ( actual >= horarioFinal):
    print('Son las',actual,', el hora de descanso')
else:
    tiempoRestante = horarioFinal - actual
    print('Faltan',tiempoRestante,'horas para ir a casa')