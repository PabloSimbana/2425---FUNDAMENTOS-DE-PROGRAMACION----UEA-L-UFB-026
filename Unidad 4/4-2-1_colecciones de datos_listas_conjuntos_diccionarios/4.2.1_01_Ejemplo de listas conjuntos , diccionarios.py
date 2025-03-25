# Ejemplos  de Listas, Diccionarios y Conjuntos en Python

# -------- LISTAS --------
print("=== LISTAS ===")
frutas = ["manzana", "banana", "cereza"]
print("Lista original:", frutas)

# Insertar
frutas.append("naranja")
print("Después de insertar 'naranja':", frutas)

# Eliminar
frutas.remove("banana")
print("Después de eliminar 'banana':", frutas)

# Borrar todos los elementos
frutas.clear()
print("Después de limpiar la lista:", frutas)

# -------- DICCIONARIOS --------
print("\n=== DICCIONARIOS ===")
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print("Diccionario original:", persona)

# Insertar
persona["profesion"] = "Ingeniera"
print("Después de insertar 'profesion':", persona)

# Eliminar un elemento
del persona["edad"]
print("Después de eliminar 'edad':", persona)

# Borrar todo el diccionario
persona.clear()
print("Después de limpiar el diccionario:", persona)

# -------- CONJUNTOS --------
print("\n=== CONJUNTOS ===")
numeros = {1, 2, 3, 4}
print("Conjunto original:", numeros)

# Insertar (add)
numeros.add(5)
print("Después de insertar 5:", numeros)

# Eliminar
numeros.discard(2)  # no lanza error si no existe
print("Después de eliminar 2:", numeros)

# Borrar todos los elementos
numeros.clear()
print("Después de limpiar el conjunto:", numeros)
