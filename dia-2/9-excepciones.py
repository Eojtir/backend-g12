try:
    print(5/'a')
except ZeroDivisionError:
    print("no se puede dividir entre cero")
except TypeError:
    print("Error tipo de dato")
except Exception:
    print("No reconosco el error")
else:#si no ingresa a ningun except
    print('Todo Bien')
finally:#entra este bien o no
    print("ingreso porque si")
print("final del archivo")

