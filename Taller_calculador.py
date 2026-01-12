# 1. Pedir el nombre del usuario
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

# 2. Guardar el dinero ganado por hora y horas trabajadas a la semana
pago_por_hora = float(input("Ingrese el dinero ganado por hora (€): "))
horas_semanales = float(input("Ingrese las horas trabajadas por semana: "))

# 3. Calcular el salario semanal
salario_semanal = pago_por_hora * horas_semanales

# 4. Calcular las ganancias anuales (52 semanas)
ganancias_anuales = salario_semanal * 52

# 5. Mostrar las ganancias anuales
print(f"\n{nombre} tiene unas ganancias anuales de: {ganancias_anuales:.2f} euros")

# 6. Pedir los gastos semanales
gastos_semanales = float(input("\nIngrese los gastos semanales (€): "))

# 7. Calcular los gastos anuales
gastos_anuales = gastos_semanales * 52

# 8 y 9. Calcular los ahorros anuales
ahorros_anuales = ganancias_anuales - gastos_anuales

# 10. Imprimir los resultados finales
print("\n--- RESUMEN FINANCIERO ---")
print(f"Ingresos anuales: {ganancias_anuales:.2f} €")
print(f"Gastos anuales: {gastos_anuales:.2f} €")
print(f"Ahorros anuales: {ahorros_anuales:.2f} €")

# Mensaje final según los ahorros
if ahorros_anuales >= 0:
    print("✔ Tiene suficiente dinero para cubrir sus gastos.")
else:
    print("✘ No tiene suficiente dinero para cubrir sus gastos.")