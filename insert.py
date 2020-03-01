def insert(arr, dim):
    alg_count = [0, 0]

    for i in range(1, dim):         # основной цикл со 2-го элемента вправо
        temp = arr[i]               # запомним элемент для сравнения
        j = i - 1
        while j >= 0:               # ищем влево ближайший меньший
            alg_count[0] += 1       # считаем операции сравнения
            if arr[j] > temp:
                alg_count[1] += 1   # считаем операции перестановки
                arr[j + 1] = arr[j] # сдвигаем элемент влево, а на его место ставим найменьший
                arr[j] = temp
            j -= 1
    return alg_count
