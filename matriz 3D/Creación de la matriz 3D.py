#Fundamentos de Programacion
#Alumna: JESENIA MONTALVAN
#TAREA: Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # MACHALA
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [   # PUYANGO
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp":33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # ARENILLAS
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp":30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 36}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp":43}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp":27 },
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

# Lista de nombres de ciudades corregida
ciudades = ["MACHALA", "PUYANGO", "ARENILLAS"]

# Recorrer ciudades y calcular promedios semanales
for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"\nPromedios de temperatura en {ciudades[ciudad_idx]}:")
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum(dia["temp"] for dia in semana)
        promedio = suma_temperaturas / len(semana)  # Cálculo del promedio
        print(f"  Semana {semana_idx + 1}: {promedio:.2f}°F")