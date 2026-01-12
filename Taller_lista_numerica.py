print("-------Ejercicio 1----------")

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

print("")   
print("-------Ejercicio 2----------")

pares_inversos = []

for n in numeros:
    if n % 2 == 0:
        pares_inversos.append(n)

pares_inversos.reverse()
print(pares_inversos)

print("")
print("-------Ejercicio 3----------")

for n in numeros:
    print(n ** 2)

print("")
print("-------Ejercicio 4----------")
print("paso 2")   

pares_inversos = [n for n in numeros if n % 2 == 0][::-1]
print(pares_inversos)

print("")
print("paso 3")

[print(n ** 2) for n in numeros]

print("")
print("-------Ejercicio 5----------")   

print("Número menor:", min(numeros))

print("")   
print("-------Ejercicio 6----------")

print("Número mayor:", max(numeros))

print("")   
print("-------Ejercicio 7----------")   

suma = 0
for n in numeros:
    suma += n

print("Suma con bucle:", suma)

print("") 

print("Suma sin bucle:", sum(numeros))

print("")
print("-------Ejercicio 8----------")

print("Índice del 8 en numeros:", numeros.index(8))

print("")
print("-------Pares Inversos----------")

print("Índice del 8 en pares_inversos:", pares_inversos.index(8))



