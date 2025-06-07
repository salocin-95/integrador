from util import *

def main():
    array = format("nombres.csv", "Apellido", "Nombre")
    # Faltaria importar a un nuevo archivo de nombres-ordenados.csv
    # Bubble sort funciona
    # bubble_sort(array)
    print(array)
    # merge_sort(array)
    quicksort(array, 0, len(array) - 1)
    print(array)
    # write(array, "nombres-ordenados.csv", "Apellido", "Nombre")

if __name__ == "__main__":
    main()
