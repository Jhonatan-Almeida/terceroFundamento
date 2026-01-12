print("-------Ejercicio 1----------")

lista = [1, 2, 3, 2, 4, 5, 1, 6]
duplicados = []
unicos = []

for x in lista:
    if x not in unicos:
        unicos.append(x)
    else:
        duplicados.append(x)

print("Duplicados:", duplicados)
print("Únicos:", unicos)

print("")
print("-------Ejercicio 2----------")

lista1 = [5, 2, 8]
lista2 = [1, 7, 3]

lista_unida = lista1 + lista2
lista_unida.sort()

print(lista_unida)

print("")
print("-------Ejercicio 3----------")

numeros = [10, 40, 30, 20, 50]

unicos = list(set(numeros))
unicos.sort(reverse=True)

print("Segundo mayor:", unicos[1])

print("")
print("-------Ejercicio 4----------")

lista = [4, 10, 2, 8, 15, 3]
n = int(input("Ingrese un número: "))

contador = 0
for x in lista:
    if x > n:
        contador += 1

print("Cantidad de números mayores:", contador)

print("")
print("-------Ejercicio 5----------")

lista = [10, 15, 20, 25, 30, 35]
n = int(input("Ingrese un número: "))

suma = 0
for x in lista:
    if x % n == 0:
        suma += x

print("Suma de divisibles:", suma)

print("")
print("-------Ejercicio 6----------")

lista = [3, 7, 12, 18, 25]
n = int(input("Ingrese un número: "))

menores = []

for x in lista:
    if x < n:
        menores.append(x)

print("Número más alto menor que", n, "es:", max(menores))

print("")
print("-------Ejercicio 7----------")

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

comunes = []

for x in lista1:
    if x in lista2:
        comunes.append(x)

print("Elementos comunes:", comunes)

print("")
print("-------Ejercicio 8----------")

lista = [23, 65, 23, 23, 10]
elemento = int(input("Ingrese el número a buscar: "))

contador = 0
for x in lista:
    if x == elemento:
        contador += 1

print("Apariciones:", contador)

print("")
print("-------Ejercicio 9----------")

lista = [-5, 3, -2, 8, 0, 7]

positivos = []

for x in lista:
    if x > 0:
        positivos.append(x)

print(positivos)

print("")
print("-------Ejercicio 10----------")

palabras = ["python", "java", "c++", "html"]

tamaños = []

for p in palabras:
    tamaños.append(len(p))

print(tamaños)

print("")
print("-------Ejercicio 11----------")

palabras = ["vicente", "prueba", "fundamentos"]

mayusculas = []

for p in palabras:
    mayusculas.append(p.upper())

print(mayusculas)



