#usamos def para definir funciones

def sumar(n1,n2):
    print(n1+n2)

sumar(25,58)

def devolver_resta(n1,n2):
    return n1-n2

resultado = devolver_resta(15,10)

print(resultado)


# > n argumentos PERO indicaremos almacenara en un diccionario el nombre del parametros y su valor y esto se

def usuarios(**params):
    print(params)

usuarios(nombre='ritjoe' , apellido='Mujica' , sexo='Masculino')

usuarios(direccion= 'las brisas' , edad = '36')


###ejercicio3333333333

print("-----------------------")

numeros = (10,20,40,55,15,12)

def promedio(*numeros):
    largo = len(numeros)
    total=0
    for numero in numeros:
        total +=  numero

    resultado= total / largo
    return resultado


respuesta = promedio(10,20,40,55,15,12)
print(respuesta)





