euros = float(input("Introduce la cantidad en euros: "))
dolares = euros * 1.2
comision = dolares * 0.10
dolares_final = dolares - comision

print("----- DESGLOSE -----")
print(f"Cantidad introducida: {euros} EU")
print(f"Equivalente en dólares: {dolares:.2f} $")
print(f"Tasa de gestión (10%): {comision:.2f} $")
print(f"Cantidad final recibida: {dolares_final:.2f} $")
print("¡Conversión completada con éxito!")