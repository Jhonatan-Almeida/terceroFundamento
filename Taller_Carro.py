# Precios de los coches (en euros)
precio_serie1 = 20000
precio_plus = 35000
precio_todoterreno = 60000

# Comisiones
comision_serie1 = 0.03
comision_plus = 0.05
comision_todoterreno = 0.07

# Entrada de datos
serie1_vendidos = int(input("Número de RBM Serie 1 vendidos: "))
plus_vendidos = int(input("Número de RBM Serie Plus vendidos: "))
todoterreno_vendidos = int(input("Número de RBM Todoterreno vendidos: "))

# Cálculo de comisiones
total_serie1 = serie1_vendidos * precio_serie1 * comision_serie1
total_plus = plus_vendidos * precio_plus * comision_plus
total_todoterreno = todoterreno_vendidos * precio_todoterreno * comision_todoterreno

# Comisión total
comision_total = total_serie1 + total_plus + total_todoterreno

# Salida de resultados
print("\n--- COMISIÓN DEL MES ---")
print(f"RBM Serie 1: {total_serie1:.2f} €")
print(f"RBM Serie Plus: {total_plus:.2f} €")
print(f"RBM Todoterreno: {total_todoterreno:.2f} €")
print(f"Comisión total del mes: {comision_total:.2f} €")