from datetime import datetime

class persona:
    nombre='ritjoe'
    edad='36'
    correo='eojtir@gmail.com'
    peso=78.2

    def decir_hora(self):
        hora,turno = datetime.now().strftime("%I-%p").split('-')

        if turno == 'AM':
            print('son las {} de la mañana'.format(hora))
        else:
            print('son las {} de la Noche'.format(hora))
            


        

    def saludar(self):
        print('hola soy {}'.format(self.nombre))
    
persona1 = persona()
persona1.nombre='benjamin'
persona1.saludar()
persona1.decir_hora()
persona2 = persona()
persona2.saludar()



print(persona1.nombre)
print(persona2.nombre)

