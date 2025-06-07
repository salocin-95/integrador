from util import *

def main():
    array = format("nombres.csv", "Apellido", "Nombre")
    # Faltaria importar a un nuevo archivo de nombres-ordenados.csv
    print(array)
    a = sorted(array)
    # Bubble sort funciona
    print(array)
    bubbleSort(array)
    print(array)
    write(array, "nombres-ordenados.csv", "Apellido", "Nombre")

if __name__ == "__main__":
    main()
