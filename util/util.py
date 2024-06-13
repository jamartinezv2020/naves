import random
from events.air_poisonous_scape import AirPoisonousScape
from events.asteroids import Asteroids
from events.mental_sickness import MentalSickness
from events.pirates import Pirates
from events.solar_storm import SolarStorm
from person.person import Person

# Definimos los eventos y sus probabilidades por cada cinturón
belts = {
    'Beta': [AirPoisonousScape(1)],  # Se incluye solo AirPoisonousScape con probabilidad 1 para el cinturón 'Beta'
    'Sigma': [],  # No hay eventos para el cinturón 'Sigma' en el ejemplo proporcionado
    'Gama': []   # No hay eventos para el cinturón 'Gama' en el ejemplo proporcionado
}

# Definimos las rutas entre cinturones
routes = {
    'Sigma': 'Beta',
    'Beta': 'Gama',
    'Gama': 'Sigma'
}

# Función para seleccionar una línea aleatoria de un archivo
def pick_line(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        file.readline()  # Saltamos la primera línea (encabezado)
        for current_line, line in enumerate(file, start=1):
            if current_line == n:
                return line.strip()
    return None  # Retorna None si n es mayor que el número de líneas en el archivo

url = "https://github.com/jamartinezv2020/naves/raw/main/applicants.txt"

# Función para seleccionar una persona aleatoria del archivo
def pick_random_person():
    # Generamos un número aleatorio entre 1 y 50000 (número máximo de líneas en el archivo)
    csv = pick_line(url, random.randint(1, 50000)).split(',')
    person = Person(csv[0], csv[1], csv[2], csv[3])  # Creamos una instancia de Person con los datos del CSV
    for i in range(4, len(csv)):
        person.add_family_member(csv[i])  # Añadimos los miembros de la familia según el CSV
    return person


