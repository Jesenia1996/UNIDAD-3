# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt y escribo algunas notas personales en él.

# Abrir el archivo en modo escritura ('w'), esto creará el archivo si no existe
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write("Nota 1: Recuerda comprar leche.\n")
    file.write("Nota 2: Llama a papá.\n")
    file.write("Nota 3: Termina el proyecto de la casa.\n")
    file.write("Nota 4: Llama al jefe.\n")
    file.write("Nota 5: Recuerdale la reunion con el invercionista.\n")
    file.write("Nota 6: Presentar proyecto.\n")
    file.write("Nota 7: Llega temprano a casa.\n")
    file.write("Nota 8: Te recomiendo leer Amor Invernal.\n")
    file.write("Nota 9: Llamar a mamá en la mañana.\n")
    file.write("Nota 10: Descansa hermano TE AMO .\n")

# Leer Archivo de Texto
# Ahora abrir el archivo my_notes.txt en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # strip() se usa para eliminar el salto de línea al final

# No es necesario cerrar el archivo manualmente cuando usamos 'with',
# ya que se cierra automáticamente al salir del bloque.