# Crear un Diccionario
informacion_persona = {
    "Nombre": "Michelle Casquete",
    "Edad": "18",
    "Ciudad": "Cuenca",
    "Profesion": "Estudiante de Ingeniería"
}

# Acceder y Modificar Valores
# Modificar la ciudad
informacion_persona["Ciudad en la que reside"] = "Cuenca."

# Agregar nueva clave-valor para profesion (ya existe, pero aquí se muestra como ejemplo)
informacion_persona["Profesión"] = "Estudiante de Ingeniería 👩"

# Verificar Existencia de Claves
if "telefono" not in informacion_persona:
    # Agregar número de celular
    informacion_persona["Numero de celular"] = "0978383947"

# Eliminar una Clave
if "edad" in informacion_persona:
    del informacion_persona["edad"]

# Imprimir el Diccionario Final
print(informacion_persona)