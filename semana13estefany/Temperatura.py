# Tu función debe recibir estos datos como parámetros y calcular la temperatura promedio de cada ciudad.

def temperatura_promedio_ciudad(ciudad_datos):
    promedios_semanales = []

    # Iteramos sobre cada semana en los datos de la ciudad
    for semana in ciudad_datos:
        # Sumamos las temperaturas de cada día en la semana
        suma_temperaturas = sum(dia["Temperatura"] for dia in semana)
        # Calculamos el promedio de temperatura de la semana y
        # lo agregamos a la lista de promedios
        promedio_semanal = suma_temperaturas / len(semana)
        promedios_semanales.append(promedio_semanal)

    # Calculamos el promedio general de la ciudad
    promedio_general = sum(promedios_semanales) / len(promedios_semanales)
    return promedio_general


#  Creamos una funcion calcular_temperatura_promedio
#  toma los datos específicos de cada ciudad y calcula el promedio de temperatura
def calcular_temperatura_promedio(datos_ciudades):
    for ciudad_datos in datos_ciudades:
        for ciudad_nombre, datos_ciudad in ciudad_datos.items():
            # calcula el promedio de temperatura
            promedio_ciudad = temperatura_promedio_ciudad(datos_ciudad)
            print(" \n ======================================================>")
            print(f"El promedio de temperatura en {ciudad_nombre} es: {promedio_ciudad:.2f}°Celsius")


datos_ciudades = [
    {"JIPIJAPA": [
        # Datos de Manta...
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 30},
            {"Dia": "Martes", "Temperatura": 23},
            {"Dia": "Miercoles", "Temperatura": 26},
            {"Dia": "Jueves", "Temperatura": 22},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 11},
            {"Dia": "Domingo", "Temperatura": 24}
        ],
        [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 29},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 12},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 21},
            {"Dia": "Domingo", "Temperatura": 14}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 25},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 76},
            {"Dia": "Jueves", "Temperatura": 12},
            {"Dia": "Viernes", "Temperatura": 22},
            {"Dia": "Sabado", "Temperatura": 31},
            {"Dia": "Domingo", "Temperatura": 14}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 15},
            {"Dia": "Martes", "Temperatura": 36},
            {"Dia": "Miercoles", "Temperatura": 56},
            {"Dia": "Jueves", "Temperatura": 22},
            {"Dia": "Viernes", "Temperatura": 12},
            {"Dia": "Sabado", "Temperatura": 11},
            {"Dia": "Domingo", "Temperatura": 54}
        ],
    ]},

    {"Atacames": [
        # Datos de Atacames
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 35},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 13},
            {"Dia": "Viernes", "Temperatura": 12},
            {"Dia": "Sabado", "Temperatura": 21},
            {"Dia": "Domingo", "Temperatura": 34}
        ],
        [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 25},
            {"Dia": "Martes", "Temperatura": 36},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 22},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 31},
            {"Dia": "Domingo", "Temperatura": 24}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 25},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 26},
            {"Dia": "Jueves", "Temperatura": 22},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 21},
            {"Dia": "Domingo", "Temperatura": 34}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 15},
            {"Dia": "Martes", "Temperatura": 86},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 12},
            {"Dia": "Viernes", "Temperatura": 17},
            {"Dia": "Sabado", "Temperatura": 11},
            {"Dia": "Domingo", "Temperatura": 13}
        ],

    ]},

    {"Guayas": [
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 35},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 12},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 21},
            {"Dia": "Domingo", "Temperatura": 24}
        ],
 [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 35},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 12},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 21},
            {"Dia": "Domingo", "Temperatura": 24}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 35},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 12},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 21},
            {"Dia": "Domingo", "Temperatura": 24}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 35},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 12},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 21},
            {"Dia": "Domingo", "Temperatura": 24}
        ]
    ]}
]

calcular_temperatura_promedio(datos_ciudades)





