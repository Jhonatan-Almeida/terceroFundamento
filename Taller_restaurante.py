# Precios del menú (en euros)
ensalada = 12
sopa = 10
dorada = 18
arroz = 14
lasana = 15
brownie = 8
helado = 6
refresco = 5.5
cafe = 3.5

print("Ingrese la cantidad consumida de cada producto:")

# Entradas
cant_ensalada = int(input("Ensalada mixta: "))
cant_sopa = int(input("Sopa de pescado: "))
cant_dorada = int(input("Dorada al horno: "))
cant_arroz = int(input("Arroz al curry: "))
cant_lasana = int(input("Lasaña de carne: "))
cant_brownie = int(input("Brownie de chocolate: "))
cant_helado = int(input("Helado: "))
cant_refresco = int(input("Refrescos: "))
cant_cafe = int(input("Café: "))

# Cálculo del total
total = (
    cant_ensalada * ensalada +
    cant_sopa * sopa +
    cant_dorada * dorada +
    cant_arroz * arroz +
    cant_lasana * lasana +
    cant_brownie * brownie +
    cant_helado * helado +
    cant_refresco * refresco +
    cant_cafe * cafe
)

# Resultado
print("\n--- TOTAL DE LA CUENTA ---")
print(f"Total a pagar: {total:.2f} €")