print("-------Ejercicio 1----------")  
n = int(input("Ingrese un número entero: "))

# Parte superior
for i in range(1, n + 1):
    print("*" * i)

# Parte inferior
for i in range(n - 1, 0, -1):
    print("*" * i)

print("")

print("-------Ejercicio 2----------")    

contraseña = "Vicente"

entrada = input("Ingrese la contraseña: ")

while entrada != contraseña:
    print("Contraseña incorrecta")
    entrada = input("Ingrese la contraseña nuevamente: ")

print("Contraseña correcta. Acceso permitido.")

print("")

print("-------Ejercicio 3----------")  
palabra = input("Ingrese una palabra: ")

for letra in palabra[::-1]:
    print(letra)

print("")

print("-------Ejercicio 4----------")

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contador = 0

for c in frase:
    if c == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")    