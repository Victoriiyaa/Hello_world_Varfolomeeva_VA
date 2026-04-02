array = [1, 2, 3, 4, 5]
n = len(array)
sum = 0
count = 0
for i in range(n):
    if i % 2 == 0:
        sum = sum + array[i]
        count = count + 1
    else:
        i = i + 1
avg = sum / count
print(f"Среднее арифметическое чисел с четными индексами равно {avg}")