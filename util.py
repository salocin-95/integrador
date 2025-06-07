import time
import csv

# tema claro

def format(file, first, last):
    with open(file, 'r') as file:
        array=[]
        csvreader = csv.DictReader(file)
        for row in csvreader:
            array.append(f"{row[first]} {row[last]}")
        print(array)
    return array    

def write(data, file, first, last):
    #Open a CSV file for writing
    with open(file, 'w', newline="") as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow([first, last])

        # Write each split name
        for full_name in data:
            last, first = full_name.split()
            writer.writerow([last, first])


def bubbleSort(array):
    start = time.time()
    n = len(array)

    # Para los elementos i de la longitud del array
    for i in range(n):
        swapped = False

        # Los ultimos elementos i ya estan en su lugar
        for j in range(0, n-i-1):
            # Se mueve a traves del array de 0 a n-i-1
            # Cambia si el elemento encontrado es mayor
            # que el siguiente elemento
            if array[j][0] > array[j+1][0]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if (swapped == False):
            end=time.time()
            break
    print(end - start)

def mergeSort(array):
    pass

def quickSort(array):
    pass 