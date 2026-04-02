array = [-1, 4, -3, -4, 3, 3]
count = 0
n = len(array)
for i in range(n):
    if array[i] > 0:
        count = count + 1
    else:
        i = i + 1
print(f"Количество положительных чисел: {count}")