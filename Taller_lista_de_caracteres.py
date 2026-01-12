print("-------Ejercicio 1----------") 

frutas = ["Manzana", "Platano", "Cereza", "Pera", "Higo", "Frambueza", "Fresa"]
print(frutas)

print("")
print("-------Ejercicio 2----------")

print("Longitud de la lista:", len(frutas))

print("")
print("-------Ejercicio 3----------") 

print("Objeto número 3:", frutas[2])

print("")
print("-------Ejercicio 4----------")

frutas[1] = "Mora"
print(frutas)

print("")
print("-------Ejercicio 5----------")

frutas.append("Mango")
print(frutas)

print("")
print("-------Ejercicio 6----------")

frutas.insert(0, "Uva")
print(frutas)

print("")
print("-------Ejercicio 7----------")

for fruta in frutas:
    print(fruta)

print("")
print("-------Ejercicio 8----------")

ultima_fruta = frutas.pop()
print("Última fruta eliminada:", ultima_fruta)
print(frutas)

print("")
print("-------Ejercicio 9----------")

for fruta in frutas:
    print(fruta)

print("")
print("-------Ejercicio 10----------")

for fruta in frutas:
    print(fruta, "-", len(fruta), "caracteres")

print("")
print("-------Ejercicio 11----------")

for fruta in frutas:
    if len(fruta) > 5:
        print(fruta)

print("")
print("-------Ejercicio 12----------")

frutas.remove("Cereza")
print(frutas)

print("")
print("-------Ejercicio 13----------")

frutas.clear()
print("Lista vacía:", frutas)