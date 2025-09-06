import random

# Parámetros
ciudades = ["Madrid", "Barcelona", "Valencia"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2

# Crear matriz 3D con temperaturas aleatorias entre 10 y 35 grados
matriz = []
for ciudad in ciudades:
    semanas = []
    for _ in range(num_semanas):
        dias = [random.randint(10, 35) for _ in dias_semana]
        semanas.append(dias)
    matriz.append(semanas)

# Calcular promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for semana in range(num_semanas):
        suma = 0
        for dia in range(len(dias_semana)):
            suma += matriz[i][semana][dia]
        promedio = suma / len(dias_semana)
        print(f"  Semana {semana+1}: Promedio = {promedio:.2f} °C")
