import csv
from faker import Faker

def format(file, first, last):
    with open(file, 'r') as file:
        array=[]
        csvreader = csv.DictReader(file)
        for row in csvreader:
            array.append(f"{row[first]} {row[last]}")
    return array    

def write(data, file, first, last):
    with open(file, 'w', newline="") as file:
        writer = csv.writer(file)

        writer.writerow([first, last])

        for full_name in data:
            last, first = full_name.split()
            writer.writerow([last, first])


def bubble_sort(array):
    n = len(array) # 2

    # Como hay dos for loops anidados se ejecuta n * n

    # Para los elementos i de la longitud del array
    for i in range(n): # n * n * lo que hay dentro del for loop
        swapped = False

        # Los ultimos elementos i ya estan en su lugar
        for j in range(0, n-i-1): # n * lo que hay dentro de este for loop
            # Se mueve a traves del array de 0 a n-i-1
            # Cambia si el elemento encontrado es mayor
            # que el siguiente elemento
            if array[j][0] > array[j+1][0]: # 3 * n * n
                array[j], array[j+1] = array[j+1], array[j] # 2
                swapped = True # 1
        if (swapped == False):
            break


def merge_sort(array):
    # Recursivo
    if len(array) > 1:
        # Divide el array en dos mitades
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        # Recursivamente
        merge_sort(left_array)
        merge_sort(right_array)

        # Merge
        # Comparamos los elementos
        i = 0 # compara el elemento de la izquierda del array izquierdo
        j = 0 # compara el elemento de la izquierda del array derecho
        k = 0 # el index del array mergeado
        while i < len(left_array) and j < len(right_array):
            # Dividie entre apellido y nombre y compara los apellidos
            if left_array[i].split()[0] < right_array[j].split()[0]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

def quicksort(array, left, right):
    if left < right:
        partition_pos = partition(array, left, right)
        quicksort(array, left, partition_pos - 1)
        quicksort(array, partition_pos + 1, right)

def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:
        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
    
    return i

# Este codigo es para crear listas de nombres aleatorias

# Reutilizamos write

lista = []
faker = Faker()
for _ in range(10):
    lista.append(f"{faker.last_name()} {faker.first_name()}")

write(lista, "nombres-10.csv", "Apellido", "Nombre")

lista = []
for _ in range(100):
    lista.append(f"{faker.last_name()} {faker.first_name()}")

write(lista, "nombres-100.csv", "Apellido", "Nombre")

lista = []
for _ in range(1000):
    lista.append(f"{faker.last_name()} {faker.first_name()}")

write(lista, "nombres-1000.csv", "Apellido", "Nombre")

lista = []
for _ in range(10000):
    lista.append(f"{faker.last_name()} {faker.first_name()}")

write(lista, "nombres-10000.csv", "Apellido", "Nombre")