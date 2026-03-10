name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")
with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write("ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    file.write(f"{name}\t\t{pressure}\n")
print()
print("Данные успешно сохранены в sensor_log.txt")