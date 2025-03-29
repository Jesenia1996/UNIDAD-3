# Creación del diccionario con información ficticia más detallada
informacion_personal = {
    "nombre": "Ramiro Montalvan",
    "edad": 38,
    "ciudad": "Estados Unidos",
    "profesion": "Ingeniero Industrial",
    "correo": "ochoa_ramiro96@gmail.com",
    "nacionalidad": "Ecuatoriano",
    "idiomas": ["Español", "Inglés"],
    "hobbies": ["Leer", "Diseñar", "Tocar guitarra"],
    "estado_civil": "Casado"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Machala"  # Se cambia de Estados Unidos a Machala

# Agregar una nueva clave-valor (como "profesion" ya existe, agregamos otra información laboral)
informacion_personal["experiencia"] = "10 años en diseño de sistemas"

# Verificar si la clave "telefono" existe en el diccionario y agregarla si no está presente
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0961337386"  # Se agrega un número personal

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final después de las modificaciones
print("Diccionario final:", informacion_personal)

