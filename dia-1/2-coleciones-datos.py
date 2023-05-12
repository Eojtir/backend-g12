#listas (arrays)
notas = [10, 20, 30,100]

variadas = [10,'Juana', 70.5, True, [1,2,3]]

print(notas)

del notas[1]

print(notas)

nota_eliminada = notas.pop(0)

print(notas)
print(nota_eliminada)

notas.remove(100)

##diccionario

persona = {
    'nombre': 'Ritjoe',
    'apellido': 'Mujica',
    'sexo':'Masculino',
    'hobies':['jugar play','Futbol', 'maratonear series'],
}
print(persona['hobies'])
print(persona.get('nacionalidad','No Existe'))


