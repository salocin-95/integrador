import time
from util import *

# Llama al algoritmo que deseamos utilizar
def llamar_algoritmo(algoritmo, lista, nombre_algoritmo, nombres_ordenados):
        start = time.perf_counter()
        algoritmo(lista)
        end = time.perf_counter()
        duration = end-start
        write(lista, nombres_ordenados, "Apellido", "Nombre")
        print(f"El algoritmo {nombre_algoritmo} tarda {duration:.6f}s para la cantidad de datos de la lista de {len(lista)} datos")

def main():
    
    # Crea un array a partir de los archivos .csv
    array_10 = format("nombres-10.csv", "Apellido", "Nombre")
    array_100 = format("nombres-100.csv", "Apellido", "Nombre")
    array_1000 = format("nombres-1000.csv", "Apellido", "Nombre")
    array_10000 = format("nombres-10000.csv", "Apellido", "Nombre")
    
    user_input = input("Elegí el algoritmo que queres usar:\n1. Bubble Sort\n2. Merge Sort\n")
    
    if user_input == "1":
        llamar_algoritmo(bubble_sort, array_10, "Bubble Sort", "nombres-10-ordenados.csv")
        llamar_algoritmo(bubble_sort, array_100, "Bubble Sort", "nombres-100-ordenados.csv")
        llamar_algoritmo(bubble_sort, array_1000, "Bubble Sort", "nombres-1000-ordenados.csv")
        llamar_algoritmo(bubble_sort, array_10000, "Bubble Sort", "nombres-10000-ordenados.csv")
        pass
    elif user_input == "2":
        llamar_algoritmo(merge_sort, array_10, "Merge Sort","nombres-10-ordenados.csv")
        llamar_algoritmo(merge_sort, array_100, "Merge Sort","nombres-100-ordenados.csv")
        llamar_algoritmo(merge_sort, array_1000, "Merge Sort","nombres-1000-ordenados.csv")
        llamar_algoritmo(merge_sort, array_10000, "Merge Sort","nombres-10000-ordenados.csv")
        pass
    else:
        print("No eligió un argumento válido.")

if __name__ == "__main__":
    main()
