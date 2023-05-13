nombre = 'Roxana'
apellido = 'Rodriguez'

if nombre == 'Roxana':
    print('Hello my friend, how are you')
else:
    print('Hello, whats??')


if nombre == 'Roxana' and apellido == 'martinez':
    print('Hello my friend Martinez, how are you')
else:
    print('Hello,'+nombre+' '+apellido+ ' whats??')


 #########################ejercicio                             n2
 # 

#ingreso = input()
#print(ingreso)


dia = input('Ingresa el dia de la Semana:')
dia = dia.upper()


if dia == 'SABADO':
    print('No se trabaja en fines de semana')
elif dia =='DOMINGO':
    print('Hoy se lava ropa')
    
else:
    print('ese dia si trabajamos')
