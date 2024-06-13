import random

def stochastic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Seleccionamos aleatoriamente un pivote
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]

        # Dividimos el array en elementos menores y mayores que el pivote
        less = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        greater = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]

        # Aplicamos el algoritmo de forma recursiva a las sublistas
        return stochastic_quicksort(less) + [pivot] + stochastic_quicksort(greater)

