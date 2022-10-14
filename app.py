from time import localtime
hora = localtime()[3]
minutos = localtime()[4]
# Horario de trabajo 9am - 2pm, 4pm - 7pm

if hora >= 19 or hora < 9:
    print(f'Es hora de estar en casa')
else:
    if minutos == 0:
        print(f'Es hora de trabajar, quedan {19-hora} horas para ir a casa')
    else:
        print(f'Es hora de trabajar, quedan {18-hora} horas {60-minutos} minutos para ir a casa')