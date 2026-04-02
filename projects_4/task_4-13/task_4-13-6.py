num = int(input("Введите число N: "))
sum = 0
i = 1
while i <= num:
    square = i * i
    sum = sum + square
    i = i + 1
print(f"Сумма квадратов первых {num} чисел равна {sum}")