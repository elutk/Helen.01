def bubble(arr, dim):
    alg_count = [0, 0]

    cnue = True                                         # continue - флаг, чтобы знать когда закончить сортировку
    while cnue:
        cnue = False
        for i in range(dim - 1):
            alg_count[0] += 1                           # считаем операции сравнения
            if arr[i] > arr[i + 1]:                     # сравниваем пару элементов
                alg_count[1] += 1                       # считаем операции перестановки
                arr[i], arr[i + 1] = arr[i + 1], arr[i] # если текущий элемент больше след. - меняем элементы местами
                cnue = True                             # если есть перестановки - продолжаем, нет - останавливаемся
    return alg_count
