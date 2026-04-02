array = [1, 3]
sum = 0
n = len(array)
for i in range(n):
    sum = sum + array[i]
avg = sum/n
print(f"Среднее арифметическое равно {avg}")