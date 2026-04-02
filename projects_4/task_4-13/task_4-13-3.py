num = float(input("Введите число: "))
i = 1
proizvedenie = 1
while i <= num:
    proizvedenie = proizvedenie * i
    i = i + 1
print(f"Факториал {num} равен {proizvedenie}")