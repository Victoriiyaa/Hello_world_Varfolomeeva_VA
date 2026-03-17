capsules = int(input("Введите общее количество произведенных капсул: "))
one_package = int(input("Введите количество капсул в одной упаковке: "))
full_packages = capsules // one_package
remains = capsules % one_package
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packages}\nОстаток капсул:\t\t{remains}")