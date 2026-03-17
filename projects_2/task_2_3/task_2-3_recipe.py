breeding_ground = input("Введите название питательной среды: ")
concentration = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации (°C): ")
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"\t{breeding_ground}\t\n")
    file.write(f"Концентрация агара (%):\t\t{concentration}\n")
    file.write(f"Температура стерилизации (°C):\t{temperature}\n")
print()
print("Файл 'recipe.txt' успешно сформирован!")