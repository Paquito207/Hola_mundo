import time

def ejercicio1 ():
    palabra = str(input("ingresa tu edad"))
    cantidad = int(input("ingrese la cantidad"))
    for i in range(cantidad):
        print("valor de la variable i: ", i+1)
        time.sleep(2)
        print(palabra)
    return palabra
ejercicio1 ()






#solicita el año actual al usuario
año_actual = int(input("Ingresa el año actual: "))
#solicita el año de nacimiento al usuario
año_nacimiento = int(input("Ingresa tu año de nacimiento: "))
#calcula la edad restando el año de nacimiento del año actual
edad = año_actual - año_nacimiento
#imprime la edad calculada
print(f"Tienes {edad} años.")
#función para imprimir cada año desde 1 hasta la edad actual
def imprimir_años(edad):
    for año in range(1, edad + 1):
        print(f" cantidad de años {año}")
#función para imprimir los años
imprimir_años(edad)