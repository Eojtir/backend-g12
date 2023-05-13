edad = input('Ingresa a tu Edad: ')
edad = int(edad)

if edad >65:
    print('No puede ingresar, es muy adulto') 
elif edad >= 18:
    print('Puedes ingresar')
    if edad >= 40 and edad <= 60:
        print('Tienes un trago de cortesia')
else:
    print ('Llamando a tus padres')


numeros = [1,10,40,50,55,3,4,9]
mayor15 = 0
menor15 = 0
for numero in numeros:
    numero = int(numero)
    if numero > 15:
        mayor15 = mayor15 + 1
    else:
        menor15 = menor15 + 1
print(f'hay {mayor15} mayores de 15 y hay {menor15} menores de 15')



##programacion orientada a objetos

