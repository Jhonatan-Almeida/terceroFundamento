tarjeta = input("Ingrese el número de la tarjeta de crédito: ")

# Separar los últimos 4 caracteres
ultimos_cuatro = tarjeta[-4:]

# Reemplazar todos los dígitos anteriores por asteriscos
oculta = "*" * (len(tarjeta) - 4) + ultimos_cuatro

print("Tarjeta enmascarada:", oculta)