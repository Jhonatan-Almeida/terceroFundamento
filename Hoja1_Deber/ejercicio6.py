ensalada = int(input("Cantidad de ensaladas: ")) * 12
sopa = int(input("Cantidad de sopas: ")) * 10
dorada = int(input("Cantidad de doradas: ")) * 18
arroz = int(input("Cantidad de arroces: ")) * 14
lasagna = int(input("Cantidad de lasañas: ")) * 15
brownie = int(input("Cantidad de brownies: ")) * 8
helado = int(input("Cantidad de helados: ")) * 6
refresco = int(input("Cantidad de refrescos: ")) * 5.5
cafe = int(input("Cantidad de cafés: ")) * 3.5

total = ensalada + sopa + dorada + arroz + lasagna + brownie + helado + refresco + cafe
print(f"Total de la cuenta: {total:.2f} EU")
print("¡Cálculo de la cuenta completado!")