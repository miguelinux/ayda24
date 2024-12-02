def bl(arr, target):
    """
    Búsqueda lineal: Busca el elemento 'target' en la lista 'arr'.
    Retorna el índice del elemento si se encuentra, o -1 si no está presente.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def bb(arr, target):
    """
    Búsqueda binaria: Busca el elemento 'target' en una lista 'arr' ordenada.
    Retorna el índice del elemento si se encuentra, o -1 si no está presente.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    numbers = [4, 2, 7, 1, 9, 3, 5]
    target = 7

    print("Lista original:", numbers)
    print("\nBúsqueda lineal (bl):")
    result_bl = bl(numbers, target)
    if result_bl != -1:
        print(f"Elemento {target} encontrado en el índice {result_bl}.")
    else:
        print(f"Elemento {target} no encontrado.")

    print("\nBúsqueda binaria (bb):")
    # Para usar búsqueda binaria, la lista debe estar ordenada
    sorted_numbers = sorted(numbers)
    print("Lista ordenada para búsqueda binaria:", sorted_numbers)
    result_bb = bb(sorted_numbers, target)
    if result_bb != -1:
        print(f"Elemento {target} encontrado en el índice {result_bb}.")
    else:
        print(f"Elemento {target} no encontrado.")

# Explicación:
# bl (Búsqueda Lineal):

# Itera sobre cada elemento de la lista hasta encontrar el objetivo (target).
# Tiempo de ejecución: O(n) en el peor caso.
# bb (Búsqueda Binaria):

# Divide la lista ordenada en mitades para buscar el objetivo.
# Tiempo de ejecución: O(log n) en el peor caso.
# Ejemplo de uso:

# La lista numbers se usa para probar ambos métodos.
# La búsqueda binaria requiere una lista ordenada, por lo que ordenamos numbers antes de llamarla.