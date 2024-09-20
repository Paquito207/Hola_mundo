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
#año_actual = int(input("Ingresa el año actual: "))
#solicita el año de nacimiento al usuario
#año_nacimiento = int(input("Ingresa tu año de nacimiento: "))
#calcula la edad restando el año de nacimiento del año actual
#edad = año_actual - año_nacimiento
#imprime la edad calculada
#print(f"Tienes {edad} años.")
#función para imprimir cada año desde 1 hasta la edad actual
#def imprimir_años(edad):
#    for año in range(1, edad + 1):
#        print(f" cantidad de años {año}")
#función para imprimir los años
#imprimir_años(edad)


#range (inicio, fin, salto):                                                numero+1
#def numeros_impares():
#    numero= int(input("ingrese el numero"))
#
#    for i in range(1, numero+1,2):
#        print(i, end=",")
#numeros_impares()




#brake rompe el ciclo for
#ejercicio
#def numeros_impares():
#    numero= int(input("ingrese el numero"))
#
#    for i in range(1, numero+1,2):
#        print(i)
#        if i == 15:
#            break;
#numeros_impares()




#ejercicio segundos
#def reloj():
#    #declaracion de la variable, su tipo, y mensaje
#    numero= int(input("ingrese el limite de segundos"))
#    for i in range(1, numero,1):
#        print(i, "segundos")
#        time.sleep(1)
#        if i == numero:
#            print("tiempo maximo")
#            break;
#reloj()




#ejercicio

#inversion_inicial = float(input("Ingrese la cantidad de inversión inicial: "))
#porcentaje_interes = float(input("Ingrese el porcentaje de interés anual: "))
#tasa_interes = porcentaje_interes / 100
#anios = int(input("Ingrese el número de años: "))
#for anio in range(1, anios + 1):
#    ganancia_anual = inversion_inicial * tasa_interes
#    inversion_inicial += ganancia_anual
#    print(f"Año {anio}: Ganancia = {ganancia_anual:.2f}, Total = {inversion_inicial:.2f}")

#def imprimir_piramide(n):
#    for i in range(n):
#        # Imprimir espacios
#        for j in range(n - i - 1):
#            print(" ", end="")
#        # Imprimir asteriscos
#        for k in range(2 * i + 1):
#            print("*", end="")
#        # Nueva línea después de cada fila
#        print()

# Solicitar al usuario la cantidad de filas
#n = int(input("Ingresa la cantidad de filas para la pirámide: "))
#imprimir_piramide(n)




#def d_c():
#    contraseña = "123456789"
#    contraseña_ingresada = ""
#    intento_ingresado = int(input("Ingrese un número de intentos: "))  
#    intento = 1
#    while contraseña_ingresada != contraseña:
#        contraseña_ingresada = input("Ingrese la contraseña: ")
#        if contraseña_ingresada == contraseña:
#            print("Contraseña correcta")
#            break
#        else:
#            print("La contraseña no coincide")
#        if intento == intento_ingresado:
#            print("Se llegó al límite de intentos")
#            break
#        intento += 1
#
#d_c()


# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")
# Inicializar el contador de letras
contador = 0
# Recorrer cada carácter en la palabra
for caracter in palabra:
    # Verificar si el carácter es una letra
    if caracter.isalpha():
        contador += 1
# Mostrar el resultado
print(f"La palabra ó oración'{palabra}' tiene {contador} letras.")

