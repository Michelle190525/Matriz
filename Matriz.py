import numpy as np

# Definimos las ciudades, días y semanas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4  # Número de semanas

# Creamos una matriz 3D con temperaturas aleatorias
# Dimensiones: [ciudades, días, semanas]
temperaturas = np.random.randint(low=15, high=35, size=(len(ciudades), len(dias), semanas))

# Calculamos el promedio de temperaturas por ciudad y semana
promedios = np.zeros((len(ciudades), semanas))

for i in range(len(ciudades)):
    for j in range(semanas):
        promedios[i][j] = np.mean(temperaturas[i, :, j])

# Mostramos los resultados
for i, ciudad in enumerate(ciudades):
    for j in range(semanas):
        print(f'Promedio de temperaturas en {ciudad} - Semana {j + 1}: {promedios[i][j]:.2f}°C')