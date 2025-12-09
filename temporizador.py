import time
numero=input("Ingrese un número de segundos para el temporizador: ")
print(f'Temporizador iniciado por {numero} segundos.')
while int(numero) > 0:
    print(f'Tiempo restante: {numero} segundos')
    time.sleep(1)
    numero = int(numero) - 1