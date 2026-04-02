numbers = int(input("Введите количество чисел: "))
max_val = int(input("Введите число №1: "))
for i in range(2, numbers + 1):
    current = int(input(f"Введите число №{i}: "))
    if current > max_val:
        max_val = current
print(f"Максимум равен: {max_val}")