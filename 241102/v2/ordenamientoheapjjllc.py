def heapify(arr, n, i):
    """
    Reorganiza el subárbol con raíz en el índice 'i' en un heap máximo.
    :param arr: Lista a ordenar.
    :param n: Número de elementos en el heap.
    :param i: Índice del nodo raíz del subárbol.
    """
    largest = i  # Inicializar el nodo raíz como el mayor
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho

    # Si el hijo izquierdo es mayor que el nodo raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es mayor que el nodo más grande encontrado hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el mayor no es el nodo raíz, intercambiar y hacer heapify recursivamente
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar
        heapify(arr, n, largest)  # Recursión

def heap_sort(arr):
    """
    Ordena una lista usando el algoritmo Heap Sort.
    :param arr: Lista a ordenar.
    """
    n = len(arr)

    # Construir un heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mover el mayor elemento al final
        heapify(arr, i, 0)  # Llamar heapify en el heap reducido

# Ejemplo de uso
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Lista original:", arr)
    heap_sort(arr)
    print("Lista ordenada:", arr)
