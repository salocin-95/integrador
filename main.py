import time
from util import *

def main():
    array_10 = format("nombres-10.csv", "Apellido", "Nombre")
    array_100 = format("nombres-100.csv", "Apellido", "Nombre")
    array_1000 = format("nombres-1000.csv", "Apellido", "Nombre")
    array_10000 = format("nombres-10000.csv", "Apellido", "Nombre")

    start = time.perf_counter()
 

    a = sorted(array_10)
    # quicksort(array_10, 0, len(array_10) - 1)
    end = time.perf_counter()
    duration = end-start
    print(f"sorted data set 10 nombres {duration:.6f}")

    start = time.perf_counter()

    a = sorted(array_100)
    # quicksort(array_100, 0, len(array_10) - 1)
    end = time.perf_counter()
    duration = end-start
    print(f"sorted data set 100 nombres{duration:.6f}")

    start = time.perf_counter()
    a = sorted(array_1000)
    # quicksort(array_1000, 0, len(array_10) - 1)
    end = time.perf_counter()
    duration = end-start
    print(f"sorted data set 1000 nombres {duration:.6f}")

    start = time.perf_counter()
    a = sorted(array_10000)
    # quicksort(array_10000, 0, len(array_10) - 1)
    end = time.perf_counter()
    duration = end-start
    print(f"sorted set 10000 nombres {duration:.6f}")


if __name__ == "__main__":
    main()
