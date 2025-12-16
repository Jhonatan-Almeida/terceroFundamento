tarjeta = input("Introduce el número de tarjeta: ")
print("Número oculto:", "*" * (len(tarjeta) - 4) + tarjeta[-4:])
print("¡Ocultación de tarjeta completada!")