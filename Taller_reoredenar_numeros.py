print("-------Ejercicio 1----------")

numero = input("Ingrese un número de más de una cifra: ")

for digito in numero:
    print(digito)

print("")
print("-------Ejercicio 2----------")

numero = input("Ingrese un número de cuatro cifras: ")

invertido = numero[::-1]

print("Número invertido:", invertido)