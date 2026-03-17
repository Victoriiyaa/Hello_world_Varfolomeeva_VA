donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
patient = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()
if donor == "I" or donor == patient or patient == "IV":
    print("Переливать кровь можно")
else:
    print("Переливать кровь нельзя")