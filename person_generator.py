# Importamos los módulos necesarios
from names_dataset import NameDataset
import random
import uuid
import os

# Creamos una instancia de NameDataset
nd = NameDataset()

# Definimos la cantidad de nombres y apellidos a utilizar
NAMES = 500
LASTNAMES = 1000

# Obtenemos los primeros 500 nombres masculinos más comunes en Estados Unidos
male_first_names = nd.get_top_names(NAMES, use_first_names=True, country_alpha2="US", gender="Male")['US']['M']

# Obtenemos los primeros 500 nombres femeninos más comunes en Estados Unidos
female_first_names = nd.get_top_names(NAMES, use_first_names=True, country_alpha2="US", gender="Female")['US']['F']

# Obtenemos los primeros 1000 apellidos más comunes en Estados Unidos
last_names = nd.get_top_names(LASTNAMES, use_first_names=False, country_alpha2="US")['US']

# Función para generar una persona aleatoria con un apellido dado
def generate_random_person(lastname):
    # Determinamos el género aleatoriamente
    gender = "Male" if random.randint(0, 1) == 0 else "Female"
    # Generamos un identificador único para la persona
    id = str(uuid.uuid4())
    # Inicializamos la información de la persona
    person = id + ","
    
    # Asignamos un nombre aleatorio según el género
    if gender == "Male":
        person += male_first_names[random.randint(0, NAMES-1)]
    else:
        person += female_first_names[random.randint(0, NAMES-1)]
    
    # Añadimos el apellido, género y edad aleatoria a la información de la persona
    person += " " + lastname
    person += "," + gender
    person += "," + str(random.randint(1, 100))
    
    # Retornamos el identificador único y la información de la persona
    return id, person

# Función para generar una familia aleatoria
def generate_random_family():
    # Inicializamos el diccionario para la familia
    family = {}
    # Probabilidad inicial de añadir más miembros a la familia
    i = 1
    # Seleccionamos un apellido aleatorio de la lista de apellidos
    lastname = last_names[random.randint(0, LASTNAMES-1)]
    
    # Mientras la probabilidad sea mayor que un número aleatorio entre 0 y 1
    while random.random() < i:
        # Generamos un nuevo miembro de la familia
        id, new_member = generate_random_person(lastname)
        # Actualizamos las relaciones familiares
        family = {member: family[member] + "," + id for member in family}
        if len(family) > 0:
            new_member += "," + ",".join(family.keys())
        # Añadimos el nuevo miembro a la familia
        family[id] = new_member
        # Disminuimos la probabilidad para el siguiente miembro
        i -= 0.1
    
    # Retornamos el diccionario de la familia
    return family

# Función para generar un archivo con n personas aleatorias
def generate(n):
    # Verificamos si la carpeta 'src' existe, y si no, la creamos
    directory = './src'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Abrimos el archivo en modo escritura
    with open(os.path.join(directory, 'applicants.txt'), 'w') as archivo:
        i = 0
        # Mientras no se hayan generado n personas
        while i < n:
            # Generamos una nueva familia
            family = generate_random_family()
            # Escribimos la información de cada miembro de la familia en el archivo
            for person in family:
                archivo.write(family[person] + '\n')
                i += 1

# Generamos un archivo con 50,000 personas aleatorias
generate(50000)
