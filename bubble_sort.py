from typing import List

def bubble_sort(array:List[int])->List[int]:
    n=len(array)
    count_pass=0
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        count_pass+=1
    return array,count_pass