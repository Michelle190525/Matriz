
archivo = open('my_notes.txt', 'w')
# Escribir notas
archivo.write("Primera nota: Recordar entregar el Practico experimental.\n")
archivo.write("Segunda nota: Estudiar para el examen .\n")
archivo.write("Tercera nota: Revisar apuntes de la clase anterior.\n")
archivo.write("Cuarta nota: Dar examen.\n")
# Cierra el archivo 
archivo.close

# Lectura de Archivo 

# Abre el archivo en modo lectura ('r')
archivo = open('my_notes.txt', 'r')

# Lee y muestra el contenido línea por línea
print("Contenido del archivo:")
linea = archivo.readline()
while linea:
    print(linea.strip())  # .strip() elimina los saltos de línea 
    linea = archivo.readline()

# Cierra el archivo 
archivo.close()
