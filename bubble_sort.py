def bubble_sort(arr):
    n = len(arr)
    number_passes = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        number_passes += 1
        if not swapped:
            break  # on arrête dès qu'aucun swap : c’est bien le vrai P_n
    return arr, number_passes
