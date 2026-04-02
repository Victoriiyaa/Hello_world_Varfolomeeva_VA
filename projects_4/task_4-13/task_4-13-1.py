a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = float(input("Введите четвертое число: "))
min = a
if b < min:
    min = b
if c < min:
    min = c
if d < min:
    min = d
print(f"Минимальное число: {min}")