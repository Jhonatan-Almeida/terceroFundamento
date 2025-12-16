serie1 = int(input("Número de RBM Serie 1 vendidos: "))
serie_plus = int(input("Número de RMB Serie Plus vendidos: "))
todoterreno = int(input("Número de RBM Todoterreno vendidos: "))

comision = (serie1 * 20000 * 0.03) + (serie_plus * 35000 * 0.05) + (todoterreno * 60000 * 0.07)

print(f"Comisión total del mes: {comision:.2f} EU")
print("¡Cálculo de comisión completado!")