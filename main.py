from bubble import bubble as b_sort
from insert import insert as i_sort
from select import select as s_sort

if __name__ == '__main__':
    arr = [6, 0, 3, 1, 2, 9, 8, 4, 5, 7, 10] # тестовый массив
    dim = len(arr) # длинна массива
    print(arr)
    alg_count = b_sort(arr, dim) # обменная сортировка
    # alg_count = i_sort(arr, dim) # сортировка включением
    # alg_count = s_sort(arr, dim) # сортировка выбором
    print(arr) # вывод отсортированного массива
    print(alg_count) # вывод кол-ва операций сровнения и перестановок
