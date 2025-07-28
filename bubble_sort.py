from typing import List

def bubble_sort(arr):
    n = len(arr)
    number_passes=0
    for i in range(n):
        swapped = False  # optimisation
        for j in range(0, n - i - 1):  # éléments non triés uniquement
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        number_passes+=1
        if not swapped:  # si aucun swap → terminé
            break
    return arr, number_passes