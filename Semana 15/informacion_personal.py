#Crear un Diccionario:
#Crea un diccionario llamado informacion_personal que contenga información ficticia
#sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
# informacionestefany= {"nombre":"estefany" , "edad ": 27 , "ciudad": "quito", "profesion":"estudiante"}

informacionestefany = {
    "nombre": "Estefany",
    "edad": 27,
    "ciudad": "Cuenca",
    "profesion": "estudiante"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacionestefany ["ciudad"] = "ambato"

# Agregar una nueva clave-valor que represente la "profesion" de la persona
informacionestefany ["profesion"] = "Estudiantes universitaria"

# Verificar si la clave "telefono" existe y, si no existe, agregarla con un número de teléfono ficticio
if "telefono" not in informacionestefany:
    informacionestefany ["telefono"] = "0984049583"

# Eliminar la clave "edad" del diccionario
if "edad" in informacionestefany:
    del informacionestefany ["edad"]

# Imprimir el diccionario resultante

print(informacionestefany)





#Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
