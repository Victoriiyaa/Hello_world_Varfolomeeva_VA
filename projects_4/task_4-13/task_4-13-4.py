num = int(input("Введите число N: "))
i = 1
sum = 0
while i <= num:
    sum = sum + i
    i = i + 1
print(f"Сумма первых {num} натуральных чисел равна {sum}")