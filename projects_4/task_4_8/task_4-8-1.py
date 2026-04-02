array = [7, 3, 8, 1, 4, 6, 2, 5]
size = len(array)
i = 0
with open("task_4-8-1.txt", "w", encoding="utf-8") as file:
    file.write(f"Исходный массив: {array}\n")
    for i in range(size):
        swapped = False
        file.write(f"Итерация №{i + 1}:\n")
        for j in range(size - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                file.write(f"{array}\n")
                swapped = True
        if not swapped:
            break
    file.write(f"Отсортированный массив: {array}")

