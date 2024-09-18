import random  # Importa el módulo random para generar elecciones aleatorias

def piedra_papel_tijera():
    global resultado  # Declara la variable resultado como global
    opciones = ["piedra", "papel", "tijera"]  # Lista de opciones disponibles
    jugador2 = random.choice(opciones)  # Selección aleatoria para el jugador 2
    jugador = random.choice(opciones)  # Selección aleatoria para el jugador 1 (corregido "ramdom" a "random")
    
    if jugador == jugador2:
        resultado = "empate"  # Si ambos jugadores eligen lo mismo, es un empate
    elif (jugador == "piedra" and jugador2 == "tijera") or (jugador == "papel" and jugador2 == "piedra") or (jugador == "tijera" and jugador2 == "papel"):
        resultado = "gana el jugador 1"  # Condiciones en las que gana el jugador 1
    else:
        resultado = "gana el jugador 2"  # Si no es empate y el jugador 1 no gana, entonces gana el jugador 2
    
    print("el jugador 1:", jugador)  # Imprime la elección del jugador 1
    print("el jugador 2:", jugador2)  # Imprime la elección del jugador 2
    print("el resultado es:", resultado)  # Imprime el resultado del juego
    return resultado  # Devuelve el resultado (corregido "result" a "resultado")

piedra_papel_tijera()  # Llama a la función para ejecutar el juego

