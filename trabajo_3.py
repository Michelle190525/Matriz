def calcular_temperatura_promedio(datos_temperaturas):
    promedios = {}
    
    for ciudad, temperaturas in datos_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio
    
    return promedios

def mostrar_temperaturas_por_semana(datos_temperaturas):
    semanas = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']
    
    print("\nTemperaturas por semana:")
    print(f"{'Ciudad':<12}", end="")
    for semana in semanas:
        print(f"{semana:<12}", end="")
    print()
    
    for ciudad, temperaturas in datos_temperaturas.items():
        print(f"{ciudad:<12}", end="")
        for temperatura in temperaturas:
            print(f"{temperatura:<12}", end="")
        print()

datos = {
    'Cuenca': [25, 27, 26, 24],
    'Azogues': [30, 29, 31, 32],
    'Ambato': [22, 21, 23, 24]
}

# Calcular promedios
promedios = calcular_temperatura_promedio(datos)

# Mostrar resultados
print("Temperaturas promedio por ciudad:")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f} °C")

# Mostrar temperaturas por semana
mostrar_temperaturas_por_semana(datos)

