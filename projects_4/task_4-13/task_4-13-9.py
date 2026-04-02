array = [1, 2, 3, 3, 0]
sum = 0
n = len(array)
for i in range(n):
    if array[i] % 2 != 0:
        sum = sum + array[i]
    else:
        i = i + 1
print(f"Сумма всех нечетных элементов в массиве равна {sum}")