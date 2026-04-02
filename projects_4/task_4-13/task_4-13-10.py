array = [1, 2, 3, 3, 0]
sum = 0
n = len(array)
for i in range(n):
    if i % 2 != 0:
        sum = sum + array[i]
    else:
        i = i + 1
print(f"Сумма элементов в массиве с нечетными индексами равна {sum}")