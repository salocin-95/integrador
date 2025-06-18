import csv
from faker import Faker

# Crea listas de nombres a partir de archivos .csv
def format(file, first, last):
    with open(file, 'r') as file:
        array=[]
        # Crea un diccionario a partir del archivo csv ingresado
        csvreader = csv.DictReader(file)
        for row in csvreader:
            array.append(f"{row[first]} {row[last]}")
    return array    

# Crea archivos .csv a partir de listas de nombres
def write(data, file, first, last):
    with open(file, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([first, last])
        for full_name in data:
            last, first = full_name.split()
            writer.writerow([last, first])

# Este codigo es para crear listas de nombres aleatorias
faker = Faker()

# Donde empieza la iteración
i = 10

# Debe ser multiplo de 10
n = 10000

while i <= n:
    lista = []
    for _ in range(i):
        lista.append(f"{faker.last_name()} {faker.first_name()}")
    # Reutilizamos write
    write(lista, f"nombres-{i}.csv", "Apellido", "Nombre")
    i = i * 10

# ------------------ Algoritmos de ordenamiento ------------------

def bubble_sort(array):

    n = len(array) 

    for i in range(n):

        swapped = False

        for j in range(0, n-i-1):
        

            if array[j][0] > array[j+1][0]:

                array[j], array[j+1] = array[j+1], array[j]

                swapped = True
        
        if (swapped == False):
            break

def merge_sort(array):
    
    if len(array) > 1:
        
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0 # compara el elemento de la izquierda del array izquierdo
        j = 0 # compara el elemento de la izquierda del array derecho
        k = 0 # el index del array mergeado

        while i < len(left_array) and j < len(right_array):
            
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