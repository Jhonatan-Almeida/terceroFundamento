nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}")

dinero_hora = float(input("Dinero ganado por hora: "))
horas_semana = int(input("Horas trabajadas por semana: "))

salario_semanal = dinero_hora * horas_semana
ganancias_anuales = salario_semanal * 52

print(f"{nombre} tiene unas ganancias anuales de: {ganancias_anuales:.2f} euros")

gastos_semanales = float(input("Introduce tus gastos semanales: "))
gasto_anual = gastos_semanales * 52

ahorros = ganancias_anuales - gasto_anual
print(f"Ahorros anuales: {ahorros:.2f} euros")

# Escenario tiempo parcial
horas_parcial = 25
gastos_reducidos = gastos_semanales * 0.75
ganancias_parcial = dinero_hora * horas_parcial * 52
gasto_anual_reducido = gastos_reducidos * 52
ahorros_parcial = ganancias_parcial - gasto_anual_reducido

print("----- ESCENARIO TIEMPO PARCIAL -----")
print(f"Ganancias: {ganancias_parcial:.2f} euros")
print(f"Gastos: {gasto_anual_reducido:.2f} euros")
print(f"Ahorros: {ahorros_parcial:.2f} euros")
print("¡Cálculo completado!")