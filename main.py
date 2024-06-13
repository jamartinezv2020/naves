# Importamos el módulo 'time' para medir el tiempo de ejecución
from time import time

# Importamos la clase 'Spaceship' del módulo 'spaceship'
from spaceship.spaceship import Spaceship

# Iniciamos el cronómetro para medir el tiempo total de ejecución del programa
start_time = time()

# Creamos una instancia de la clase 'Spaceship'
spaceship = Spaceship()

# Medimos el tiempo de selección de los viajeros
selection_start_time = time()
spaceship.select_travelers()  # Seleccionamos a los viajeros
selection_end_time = time()

# Medimos el tiempo de viaje
travel_start_time = time()
spaceship.travel()  # Realizamos el primer viaje
spaceship.travel()  # Realizamos el segundo viaje
spaceship.travel()  # Realizamos el tercer viaje
travel_end_time = time()

# Finalizamos el cronómetro para el tiempo total de ejecución del programa
end_time = time()

# Mostramos la distribución de habitaciones de la nave
spaceship.show_rooms()
# Imprimimos la ruta recorrida por la nave
print("Coursed route: ", spaceship.route)
# Calculamos y mostramos el tiempo total para seleccionar a los viajeros
print('Total time to select the voyagers: ', selection_end_time - selection_start_time, ' seconds')
# Calculamos y mostramos el tiempo total para realizar los viajes
print('Total time to go through each one belt of events and type of event: ', travel_end_time - travel_start_time, ' seconds')
# Calculamos y mostramos el tiempo total de ejecución del programa
print('Total running time of the whole algorithm: ', end_time - start_time, ' seconds')

