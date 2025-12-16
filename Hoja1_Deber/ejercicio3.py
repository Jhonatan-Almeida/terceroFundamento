def convertir_a_segundos(minutos, segundos, centesimas):
    return minutos * 60 + segundos + centesimas / 100

hannah = convertir_a_segundos(8, 3, 10)
jackie = convertir_a_segundos(12, 7, 8)
kimberley = convertir_a_segundos(9, 14, 3)

print("----- RESULTADOS -----")
print(f"Hannah Neise: {100/hannah:.2f} m/s")
print(f"Jackie Narracott: {100/jackie:.2f} m/s")
print(f"Kimberley Bos: {100/kimberley:.2f} m/s")
print("¡Cálculo de velocidades completado!")