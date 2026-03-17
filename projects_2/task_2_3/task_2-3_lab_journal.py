name = input("Введите ФИО исследователя: ")
date = input("Введите дату: ")
title = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")
width = 60
line = f"+{'-' * (width - 2)}+"
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(f"{line}\n")
    file.write(f"| {'Электронный лабораторный журнал':<{width - 3}}|\n")
    file.write(f"{line}\n")
    file.write(f"| ФИО исследователя: {name:<{width - 23}} |\n")
    file.write(f"| Дата: {date:<{width - 23}}              |\n")
    file.write(f"| Эксперимент: {title:<{width - 22}}      |\n")
    file.write(f"{line}\n")
    file.write(f"| Вывод: {conclusion:<{width - 17}}       |\n")
    file.write(f"{line}\n")